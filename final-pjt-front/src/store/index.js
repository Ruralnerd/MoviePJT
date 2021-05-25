import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    mymovies:[],
    removies:[],
    savemovies:[1],
  },
  mutations: {
    SAVE_MOVIE: function(state, movie) {
      state.mymovies.push(movie)
    },
    SAVE_ID: function(state, movie) {
      state.savemovies.unshift(movie)
      state.savemovies.pop()
    },
  },
  actions: {
    saveMovie: function({ commit }, movie) {
      commit('SAVE_MOVIE', movie)
    },
    saveId: function({ commit }, movie) {
      commit('SAVE_ID', movie)
    },
  },
  getter: {
    recommendMovie: function(state) {
      if (state.mymovies.vote_average > 5) {
        state.removies.push(state.mymovies)
      }
    }
  },
  created: function () {
    this.saveMovie()
    this.saveId()
  },
  modules: {
  }
})
