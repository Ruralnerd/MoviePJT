import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    movies:[],
    mymovies:[],
    removies:[],
    savemovies:[1],
    // savetitle:[],
  },
  mutations: {
    SAVE_MOVIE: function(state, movie) {
      state.mymovies.push(movie)
    },
    SAVE_ID: function(state, movie) {
      state.savemovies.unshift(movie)
      state.savemovies.pop()
    },
    GET_MOVIES: function(state, movies) {
      // state.movies.push(movies)
      state.movies = movies
    },
    // SAVE_TITLE: function(state, movie) {
    //   state.savetitle.push(movie)
    // }
  },
  actions: {
    saveMovie: function({ commit }, movie) {
      commit('SAVE_MOVIE', movie)
    },
    saveId: function({ commit }, movie) {
      commit('SAVE_ID', movie)
    },
    getMovies: function({ commit }) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/movies/movie_list/'
      })
        .then((response) => {
          console.log(response)
          commit('GET_MOVIES', response.data)
        })
    },
    // saveTitle: function({ commit }, movie) {
    //   commit('SAVE_TITLE', movie)
    // }
  },
  getter: {
    recommendMovie: function(state) {
      if (state.mymovies.vote_average > 5) {
        state.removies.push(state.mymovies)
      }
    }
  },
  modules: {
  }
})
