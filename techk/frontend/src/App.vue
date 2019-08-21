<template>
	<div id="app">
		<h1>Books Scrapper</h1>
		<div class="row scrapper-container">
			<div class="col-4"></div>
			<div class="col-4">
				<ScrappingButtons />
			</div>
		</div>
  <b-alert v-if="fallback" show variant="warning">Nota: Scrapping actualmente no realizado, por lo que se muestran datos predefinidos. Favor de presionar "Start Scrapping", y esperar a que se realice el proceso de Scrapping</b-alert>
		<BooksFilter />
		<div class="separator"></div>
		<Apptable />
	</div>
</template>

<script>
import Apptable from './components/Table.vue'
import BooksFilter from './components/BooksFilter.vue'
import ScrappingButtons from './components/ScrappingButtons.vue'

export default {
  name: 'app',
  components: {
		Apptable,
		BooksFilter,
		ScrappingButtons
  },
	computed: {
		fallback: {
			get() {
				return this.$store.getters.fallback
			}
		}
	}
}
</script>

<style>
#app {
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.scrapper-container {
	margin-bottom: 40px;
}

.separator{
	margin-bottom: 40px;
}
</style>


