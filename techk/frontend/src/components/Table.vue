<template>
	<div id="apptable">
		<h2>Vue Table</h2>	
		<div class="search-wrapper">
			<input type="text" v-model="search" placeholder="Search title.."/>
		</div>
		<table>
			<thead>
				<tr>
					<th v-for="key in columns" v-bind:key="key">
						{{ key }}
					</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="entry in filteredList" v-bind:key="entry">
						<td> <img :src="entry.thumbnail"></img> </td>
						<td>{{entry.title}}</td>
						<td>{{entry.price}}</td>
						<td>{{entry.stock}}</td>
						<td>{{entry.upc}}</td>
						<td><button @click="removeBook(entry.id)">X</button></td>
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
			columns: ['thumbnail','title', 'price', 'stock', 'upc','delete'],
			search: '',
			books: [
			]
		}},
	mounted () {
		const that = this
		this.updateBooks(1)
		this.$store.subscribe((mutation, state) => {
			console.log('suscribed')
			that.updateBooks(state.category)
		})
	},
	computed: {
		filteredList() {
      return this.books.filter(book => {
        return book.title.toLowerCase().includes(this.search.toLowerCase())
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
body {
  font-family: Helvetica Neue, Arial, sans-serif;
  font-size: 14px;
  color: #444;
}

table {
  border: 2px solid #42b983;
  border-radius: 3px;
  background-color: #fff;
}

th {
  background-color: #42b983;
  color: rgba(255,255,255,0.66);
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

td {
  background-color: #f9f9f9;
}

th, td {
  min-width: 120px;
  padding: 10px 20px;
}

th.active {
  color: #fff;
}

th.active .arrow {
  opacity: 1;
}

.arrow {
  display: inline-block;
  vertical-align: middle;
  width: 0;
  height: 0;
  margin-left: 5px;
  opacity: 0.66;
}

.arrow.asc {
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-bottom: 4px solid #fff;
}

.arrow.dsc {
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-top: 4px solid #fff;
}

img {
	height: 50px;
}
</style>
