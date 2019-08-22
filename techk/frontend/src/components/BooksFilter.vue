<template>
	<div id="booksfilter">
		<div class="row">
			<div class="col-3">
				Category: 
			</div>
			<div class="col-3">
				<select :value="category" class="form-control" id="categories" name="category" @change="onCategoryChange($event)">
					<option v-for="category in categories" :key="category.id" :value="category.id">{{category.name}}</option>
				</select>
			</div>
		</div>
		<div class="row search-wrapper">
			<div class="col-3">
				Filter:
			</div>
			<div class="col-3">
				<select class="form-control" @change="onFilterChange($event)">
					<option v-for="opt in searchoptions" :key="opt" :value="opt">{{opt}}</option>
				</select>
			</div>
			<div class="col-4">
				<input class="form-control" type="text" v-model="search" :placeholder="'Search '+this.$store.getters.searchfield+'..'"/>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'CategoriesDropdown',
	data () {
		return {
			categories: [ ],
			searchoptions: ['title', 'price', 'stock', 'upc', 'description'],
			fallback: true
		}},
	created () {
		let that = this
		this.updateCategories()
		this.$store.subscribe((mutation) => {
			if (mutation.type === 'changeScrapped'){
				that.updateCategories()
			}
		})
	},
	computed: {
		search: {
			set(value) {
				this.$store.commit('changeSearch', value)
			},
			get() {
				return this.$store.getters.search
			}
		},
		category: {
			get() {
				return this.$store.getters.category
			}
		}
	},
	methods: {
		/**
		 * Realiza un llamado a la API, para poder obtener el listado de Categorias de 
		 * la plataforma.
		 * En caso de no tener categorias en la base de datos, se retorna un objeto "fallback",
		 * que se define en el archivo books.json
		 */
		updateCategories(){
			var that = this
			axios
				.get('/api/categories/?format=json')
				.then(response => {
					if (response.data.length > 0) {
						that.categories = response.data
						that.$store.commit('changeFallback', false)
						that.$store.commit('changeCategory', response.data[0].id)
					}
					else {
						axios.get('/api/fallback')
							.then(response => {
								that.categories = response.data.categories
								that.$store.commit('changeCategory', response.data.categories[0].id)
							})
					}
				})
		},
		onCategoryChange(e) {
			this.$store.commit('changeCategory', e.target.value)
		},
		onFilterChange(e) {
			this.$store.commit('changeSearchfield', e.target.value)
		}
	}
}
</script>

<style>
</style>


