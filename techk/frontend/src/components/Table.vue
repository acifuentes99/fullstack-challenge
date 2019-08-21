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
					<td> <img :src="entry.thumbnail"></img> </td>
					<td>{{entry.title}}</td>
					<td>{{entry.price}}</td>
					<td>{{entry.stock}}</td>
					<td>{{entry.upc}}</td>
					<td>
						<b-button size="sm" v-b-modal="'modal-'+entry.id">Description</b-button>
						<b-modal :id="'modal-'+entry.id" :title="entry.title">
							<p class="my-4">{{entry.description}}</p>
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
	mounted () {
		const that = this
		this.updateBooks(1)
		this.$store.subscribe((mutation, state) => {
			that.updateBooks(state.category)
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
	methods: {
		updateBooks(category_id) {
			axios
				.get('/api/books/category/'+category_id+'?format=json')
				.then(response => (this.books = response.data))
		},
		removeBook(book_id) {
			let that = this
			axios
				.delete('/api/books/'+book_id+'/')
				.then(() => {that.updateBooks(that.$store.getters.category)})
				.catch((err) => console.log(err))
		}
	}
}
</script>

<style>
img {
	height: 50px;
}
</style>
