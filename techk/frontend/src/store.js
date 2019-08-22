import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
const store = new Vuex.Store({
	state: {
		category: '',
		search: '',
		searchfield: 'title',
		fallback: true,
		scrapped: false
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
		},
		changeFallback(state, fallback) {
			state.fallback = fallback
		},
		changeScrapped(state, scrapped) {
			state.scrapped = scrapped
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
		},
		fallback (state) {
			return state.fallback
		},
		scrapped (state) {
			return state.scrapped
		}
	}
})
export default store
