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
    rmovie:[],
    updatearticle:null,
    savemovietitles:null,
    savemovies: [],
    latestmovies: null,
    popularmovies: null,
    todaymovies: null,
    myinfo: null,
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
    ARTICLE_UPDATE: function(state, detail) {
      state.updatearticle = detail
    },
    R_MOVIE: function(state, movie) {
      state.rmovie = movie
    },
    INFO_SAVE: function(state, info) {
      state.myinfo = info
    },
    INFO_DELETE: function(state) {
      state.myinfo.pop()
    }
  },
  actions: {
    saveMovie: function({ commit }, movie) {
      commit('SAVE_MOVIE', movie)
    },
    infoDelete: function({ commit }) {
      commit('INFO_DELETE')
    },
    saveId: function({ commit }, movie) {
      commit('SAVE_ID', movie)
    },
    rmovie: function({ commit }, movie) {
      commit('R_MOVIE', movie)
    },
    articleUpdate: function({ commit }, detail) {
      commit('ARTICLE_UPDATE', detail)
    },
    infosave: function({ commit }, info) {
      commit('INFO_SAVE', info)
    },
    getMovies: function({ commit }) {
      const ck = localStorage.getItem('vuex')
      // console.log(JSON.parse(ck))
      if (ck) {
        commit('GET_MOVIES', JSON.parse(ck).movies)
      } else {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/movie_list/'
      })
        .then((response) => {
          console.log(response)
          commit('GET_MOVIES', response.data)
        })
      }
    },
    getLatest: function({ commit }) {
      const ck = localStorage.getItem('vuex')
      if (ck) {
        commit('GET_LATEST', JSON.parse(ck).latestmovies)
      } else {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/recommend/latest_movies/'
      })
        .then((response) => {
          console.log(response)
          commit('GET_LATEST', response.data)
        })
      }
    },
    getPopular: function({ commit }) {
      const ck = localStorage.getItem('vuex')
      if (ck) {
        commit('GET_POPULAR', JSON.parse(ck).popularmovies)
      } else {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/recommend/popular_movies/'
      })
        .then((response) => {
          console.log(response)
          commit('GET_POPULAR', response.data)
        })
      }
    },
    getToday: function({ commit }) {
      const ck = localStorage.getItem('vuex')
      if (ck) {
        commit('GET_TODAY', JSON.parse(ck).todaymovies)
      } else {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/recommend/today_movies/'
      })
        .then((response) => {
          console.log(response)
          commit('GET_TODAY', response.data)
        })
      }
    },
  },
  getter: {
  },
  modules: {
  }
})
