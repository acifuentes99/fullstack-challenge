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
					<td><img :src="entry.thumbnail_url"></td>
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
		/**
		 * Retorna los libros que cumplen con el criterio de busqueda seleccionado por el
		 * usuario
		 *
		 * @returns {array} Filtro de libros respecto a criterio
		 */
		filteredList() {
			return this.books.filter(book => {
				return book[this.$store.getters.searchfield].toString().toLowerCase()
					.includes(this.$store.getters.search.toString().toLowerCase())
			})
		},
	},
	filters: {
		/**
		 * Revisa si la expresión para precio entregado esta correcto, esto debido a que el
		 * JSON de fallback tiene el signo de moneda integrado, y se debe remover para mostrar
		 * precios
		 *
		 * @param {number} price Precio entregado por la consulta realizada (fallback o a la API)
		 */
		pricefilter(price) {
			if (price.toString().charAt(0) === '£'){
				return price.substr(1)
			}
			return price
		}
	},
	methods: {
		/**
		 * Actualiza el listado de libros, dependiendo de la categoria seleccionada
		 *
		 * @param {number} category_id ID de la categoria la cual se utilizará como filtro
		 */
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
		/**
		 * Remueve libros de la base de datos, a través de la API de libros
		 *
		 * @param {number} book_id ID del libro el cual borrar
		 */
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
