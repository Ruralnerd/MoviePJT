import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '../views/Main.vue'
import Recommended from '../views/Recommended.vue'
import Signin from '../views/Signin.vue'
import Signout from '../views/Signout.vue'
import Signup from '../views/Signup.vue'
import MyMovieList from '../views/MyMovieList.vue'

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
  {
    path: '/mymovielist',
    name: 'MyMovieList',
    component: MyMovieList
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
