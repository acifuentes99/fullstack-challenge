<template>
	<div id="app">
		<h1>Books Scrapper</h1>
		<div class="row scrapper-container">
			<div class="col-4"></div>
			<div class="col-4">
				<ScrappingButtons />
			</div>
		</div>
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
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
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


