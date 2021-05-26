import Vue from 'vue'
import VueRouter from 'vue-router'
import Cover from '../views/Cover.vue'
import Main from '../views/movies/Main.vue'
import RecommendedMovieList from '../views/movies/RecommendedMovieList.vue'
import YoutubeSearch from '../views/movies/YoutubeSearch.vue'

import Community from '../views/community/Community.vue'


import Article from '../components/community/Article.vue'
import ArticleDetail from '../components/community/ArticleDetail.vue'

import ArticleForm from '../components/community/ArticleForm.vue'
import ArticleUpdateForm from '../components/community/ArticleUpdateForm.vue'

import Signin from '../views/accounts/Signin.vue'
import Signup from '../views/accounts/Signup.vue'



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Cover',
    component: Cover
  },
  {
    path: '/main',
    name: 'Main',
    component: Main
  },
  {
    path: '/recommendedmovielist',
    name: 'RecommendedMovieList',
    component: RecommendedMovieList
  },
  {
    path: '/youtubesearch',
    name: 'YoutubeSearch',
    component: YoutubeSearch
  },
  {
    path: '/community',
    name: 'Community',
    component: Community
  },
  {
    path: '/article',
    name: 'Article',
    component: Article
  },
  {
    path: '/articledetail/:id',
    name: 'ArticleDetail',
    component: ArticleDetail,
    props: true
  },
  {
    path: '/articleform',
    name: 'ArticleForm',
    component: ArticleForm
  },
  {
    path: '/articleupdateform/:id',
    name: 'ArticleUpdateForm',
    component: ArticleUpdateForm,
    props: true
  },
  {
    path: '/signin',
    name: 'Signin',
    component: Signin
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
