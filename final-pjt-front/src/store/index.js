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

    // 이 아래쪽 부분 주석처리된 코드들은, 한번 갱신 후에는 axios요청을 보내지 않는 코드로 만들었는데
    // 이미 vuex에 데이터가 '있으면' 작동을 안하는데 '없을'때도 작동을 안해서 주석처리 한 후에 git에 업로드 해놓겠습니다
    // 주석처리하면 메인에 갈때마다 요청을 보내지만..코드 구동에는 문제 없습니다
    getMovies: function({ commit }) {
      // const ck = localStorage.getItem('vuex')
      // console.log(JSON.parse(ck))
      // if (ck) {
      //   commit('GET_MOVIES', JSON.parse(ck).movies)
      // } else {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/movie_list/'
      })
        .then((response) => {
          console.log(response)
          commit('GET_MOVIES', response.data)
        })
      // }
    },
    getLatest: function({ commit }) {
      // const ck = localStorage.getItem('vuex')
      // if (ck) {
      //   commit('GET_LATEST', JSON.parse(ck).latestmovies)
      // } else {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/recommend/latest_movies/'
      })
        .then((response) => {
          console.log(response)
          commit('GET_LATEST', response.data)
        })
      // }
    },
    getPopular: function({ commit }) {
      // const ck = localStorage.getItem('vuex')
      // if (ck) {
      //   commit('GET_POPULAR', JSON.parse(ck).popularmovies)
      // } else {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/recommend/popular_movies/'
      })
        .then((response) => {
          console.log(response)
          commit('GET_POPULAR', response.data)
        })
      // }
    },
    getToday: function({ commit }) {
      // const ck = localStorage.getItem('vuex')
      // if (ck) {
      //   commit('GET_TODAY', JSON.parse(ck).todaymovies)
      // } else {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/recommend/today_movies/'
      })
        .then((response) => {
          console.log(response)
          commit('GET_TODAY', response.data)
        })
      // }
    },
  },
  getter: {
  },
  modules: {
  }
})
