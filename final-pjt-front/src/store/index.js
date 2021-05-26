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
    savemovietitles:null,
    savemovies: null,
    latestmovies: null,
    popularmovies: null,
    todaymovies: null,
    
    // savetitle:[],
  },
  mutations: {
    SAVE_MOVIE: function(state, movie) {
      state.mymovies.push(movie)
    },
    SAVE_ID: function(state, movie) {
      state.savemovies = movie
    },
    GET_MOVIES: function(state, movies) {
      state.movies = movies
    },
    GET_LATEST: function(state, movies) {
      state.latestmovies = movies
    },
    GET_POPULAR: function(state, movies) {
      state.popularmovies = movies
    },
    GET_TODAY: function(state, movies) {
      state.todaymovies = movies
    },
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
        url: 'http://127.0.0.1:8000/movies/movie_list/'
      })
        .then((response) => {
          console.log(response)
          commit('GET_MOVIES', response.data)
        })
    },
    getLatest: function({ commit }) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/recommend/latest_movies/'
      })
        .then((response) => {
          console.log(response)
          commit('GET_LATEST', response.data)
        })
    },
    getPopular: function({ commit }) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/recommend/popular_movies/'
      })
        .then((response) => {
          console.log(response)
          commit('GET_POPULAR', response.data)
        })
    },
    getToday: function({ commit }) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/recommend/today_movies/'
      })
        .then((response) => {
          console.log(response)
          commit('GET_TODAY', response.data)
        })
    },
  },
  getter: {
  },
  modules: {
  }
})
