<template>
	<div id="scrappingbuttons">
		<button @click="scrape()">{{message}}</button>
	</div>
</template>

<script>
import axios from 'axios'
export default {
	name: 'ScrappingButtons',
	data () {
		return {
			message: 'Start Scrapping'
		}
	},
	methods: {
		scrape: () => {
			this.message = 'Scrapping Books'
			axios
			.get('/scrapebooks')
			.then(() => (this.message = 'Books Scrapped!'))
		}
	}
}
</script>
