<template>
	<div id="scrappingbuttons">
		<div class="row">
			<div class="col-4"></div>
			<div class="col-4">
			<div class="row notflex">
				<span class="pagetext">Scrapping page number ({{pages}}):</span>
				<input type="range" name="number_pages" v-model="pages" min="1" max="50">
			</div>
			
			</div>
			<div class="row">
			</div>
		</div>

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
			loading: false,
			pages: 5
		}
	},
	computed: {
		fallback: {
			get(){
				return this.$state.getters.fallback
			}
		}
	},
	methods: {
		/**
		 * Ejecuta la acción de Scrapping en el Backend, a través de un request GET. El usuario 
		 * puede también seleccionar la cantidad de páginas que realizará el Scrapping, para no
		 * esperar todo el contenido en su totalidad.
		 */
		scrape()  {
			let that = this
			this.loading = true
			this.message = 'Scrapping Books...'
			axios
			.get('/scrape/books/'+this.pages+'/')
			.then(() => {
				that.message = 'Scrapping Finished! (Press to scrape again)'
				that.loading = false
				that.$store.commit('changeScrapped', true)
			})
		}
	}
}
</script>

<style>
#scrappingbuttons{
	position: relative;
	text-align: center;
}
.spinner{
	position: absolute;
	margin-left: 50px;
}
.scrapepage{
	display: inline-block !important;
}
.pagetext{
	margin-right: 20px;
}
.notflex{
	display: block !important;
}
</style>
