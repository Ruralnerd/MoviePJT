import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '../views/movies/Main.vue'
import Recommended from '../views/movies/Recommended.vue'
import MyMovieList from '../views/movies/MyMovieList.vue'
import MovieAdd from '../views/movies/MovieAdd.vue'

import Community from '../views/community/Community.vue'


import Article from '../components/community/Article.vue'
import ArticleDetail from '../components/community/ArticleDetail.vue'

import ArticleForm from '../components/community/ArticleForm.vue'

import Signin from '../views/accounts/Signin.vue'
import Signout from '../views/accounts/Signout.vue'
import Signup from '../views/accounts/Signup.vue'



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Main',
    component: Main
  },
  {
    path: '/recommended',
    name: 'Recommended',
    component: Recommended
  },
  {
    path: '/mymovielist',
    name: 'MyMovieList',
    component: MyMovieList
  },
  {
    path: '/movieadd',
    name: 'MovieAdd',
    component: MovieAdd
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
    path: '/signin',
    name: 'Signin',
    component: Signin
  },
  {
    path: '/signout',
    name: 'Signout',
    component: Signout
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
