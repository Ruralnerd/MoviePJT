import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    mymovies:[],
    removies:[],
  },
  mutations: {
    SAVE_MOVIE: function(state, movie) {
      state.mymovies.push(movie)
    },
  },
  actions: {
    saveMovie: function({ commit }, movie) {
      commit('SAVE_MOVIE', movie)
    },
  },
  getter: {
    recommendMovie: function(state) {
      if (state.mymovies.vote_average > 9) {
        state.removies.push(state.mymovies)
      }

    }
    
  },
  modules: {
  }
})
