<template>
  <div id="app">
		<h1>Books Scrapper</h1>
		<ScrappingButtons />
		<CategoriesDropdown />
		<Apptable />
  </div>
</template>

<script>
import Apptable from './components/Table.vue'
import CategoriesDropdown from './components/CategoriesDropdown.vue'
import ScrappingButtons from './components/ScrappingButtons.vue'

export default {
  name: 'app',
  components: {
		Apptable,
		CategoriesDropdown,
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
</style>


