<template>
	<div id="scrappingbuttons">
		<b-button @click="scrape()" variant="primary">{{message}}</b-button>
			<b-spinner v-if="loading" class="spinner" variant="primary" label="Spinning"></b-spinner>
	</div>
</template>

<script>
import axios from 'axios'
export default {
	name: 'ScrappingButtons',
	data () {
		return {
			message: 'Start Scrapping',
			loading: false
		}
	},
	methods: {
		scrape()  {
			let that = this
			this.loading = true
			this.message = 'Scrapping Books...'
			axios
			.get('/scrape/books')
			.then(() => {
				that.message = 'Scrapping Finished!'
				that.loading = false
			})
		}
	}
}
</script>

<style>
scrappingbuttons{
	position: relative;
}
.spinner{
	position: absolute;
	margin-left: 50px;
}
</style>
