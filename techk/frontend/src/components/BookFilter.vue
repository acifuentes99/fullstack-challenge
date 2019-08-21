<template>
	<div id="bookfilter">
		<div class="row">
			<div class="col-3">
				Category: 
			</div>
			<div class="col-3">
				<select class="form-control" id="categories" name="category" @change="onCategoryChange($event)">
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
						<option v-for="opt in searchoptions" :value="opt">{{opt}}</option>
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
			categories: [
				{id: 1, title: 'sadfdsa'}
			],
			searchoptions: ['title', 'price', 'stock', 'upc', 'description'],
		}},
	mounted () {
		var that = this
		axios
		.get('/api/categories/?format=json')
			.then(response => {
				that.categories = response.data
				that.$store.commit('changeCategory', response.data[0].id)
			})
	},
	computed: {
		search: {
			set(value) {
				this.$store.commit('changeSearch', value)
			}
		}
	},
	methods: {
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

.search-wrapper{
	margin-bottom: 40px;
}
</style>


