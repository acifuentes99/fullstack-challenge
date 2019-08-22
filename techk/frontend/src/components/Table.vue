<template>
	<div id="apptable">

		<table class="table">
			<thead class="table-dark">
				<tr class="bg-success">
					<th v-for="key in columns" v-bind:key="key">
						{{ key }}
					</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="entry in filteredList" v-bind:key="entry.id">
					<td> <img :src="entry.thumbnail_url"></img> </td>
					<td>{{entry.title}}</td>
					<td>£{{entry.price | pricefilter}}</td>
					<td>{{entry.stock}}</td>
					<td>{{entry.upc}}</td>
					<td>
						<b-button size="sm" v-b-modal="'modal-'+entry.id">Description</b-button>
						<b-modal :id="'modal-'+entry.id" :title="entry.title">
							<p class="my-4">{{entry.product_description}}</p>
						</b-modal>
					</td>
					<td><font-awesome-icon @click="removeBook(entry.id)" icon="trash-alt"></font-awesome-icon></td>
				</tr>
			</tbody>
		</table>
	</div>
</template>

<script>
import axios from 'axios'
export default {
	name: 'Apptable',
	data () {
		return {
			columns: ['thumbnail','title', 'price', 'stock', 'upc', 'description', 'delete'],
			books: []
		}},
	beforeMount () {
		const that = this
		this.updateBooks(1)
		this.$store.subscribe((mutation, state) => {
			if (mutation.type === 'changeCategory'){
				that.updateBooks(state.category)
			}
		})
	},
	computed: {
		filteredList() {
			return this.books.filter(book => {
				return book[this.$store.getters.searchfield].toString().toLowerCase()
					.includes(this.$store.getters.search.toString().toLowerCase())
			})
		},
	},
	filters: {
		pricefilter(price) {
			if (price.toString().charAt(0) === '£'){
				return price.substr(1)
			}
			return price
		}
	},
	methods: {
		updateBooks(category_id) {
			if(!this.$store.getters.fallback) {
				axios
					.get('/api/books/category/'+category_id+'?format=json')
					.then(response => (this.books = response.data))
			}
			else {
				axios.get('/api/fallback')
					.then(response => {
						this.books = response.data.books.filter(
							book => book.category_id.toString() === category_id.toString())
					})
			}
		},
		removeBook(book_id) {
			let that = this
			axios
				.delete('/api/books/'+book_id+'/')
				.then(() => {that.updateBooks(that.$store.getters.category)})
		}
	}
}
</script>

<style>
img {
	height: 50px;
}
</style>
