import Vue from 'vue'
import Vuex from 'vuex'
//https://medium.com/js-dojo/vuex-and-vue-bread-and-butter-4519a21e95ce

Vue.use(Vuex)
const store = new Vuex.Store({
	state: {
		category: '',
		search: '',
		searchfield: 'title'
	},
	mutations: {
		changeCategory(state, category) {
			state.category = category
		},
		changeSearch(state, search) {
			state.search = search
		},
		changeSearchfield(state, searchfield) {
			state.searchfield = searchfield
		}
	},
	actions: {
		changeAction (context, category) {
			context.commit('changeCategory', category)
		}
	},
	getters: {
		category (state) {
			return state.category
		},
		search (state) {
			return state.search
		},
		searchfield (state) {
			return state.searchfield
		}
	}
})
export default store
