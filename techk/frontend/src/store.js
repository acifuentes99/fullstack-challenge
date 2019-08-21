import Vue from 'vue'
import Vuex from 'vuex'
//https://medium.com/js-dojo/vuex-and-vue-bread-and-butter-4519a21e95ce

Vue.use(Vuex)
const store = new Vuex.Store({
	state: {
		category: ''
	},
	mutations: {
		changeCategory(state, category) {
			state.category = category
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
		}
	}
})
export default store
