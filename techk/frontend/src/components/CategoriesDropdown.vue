<template>
  <div id="categoriesdropdown">
		Category: 
<select id="categories" name="category" @change="onChange($event)">
	<option v-for="category in categories" :key="category.id" :value="category.id">{{category.name}}</option>
</select>

		vuex: {{$store.getters.category}}
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
			]
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
	methods: {
		onChange(e) {
			this.$store.commit('changeCategory', e.target.value)
		}
	}
}
</script>

<style>
</style>


