import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// bootstrap을 사용하기 위한 코드1
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// vue-glide를 사용하기 위한 코드1
import VueGlide from 'vue-glide-js'
import 'vue-glide-js/dist/vue-glide.css'

//font-awesome을 사용하기 위한 코드1
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

// vue-lodash 사용하기 위한 코드 1
import VueLodash from 'vue-lodash'
import lodash from 'lodash'

// import StarRating from 'vue-star-rating'

// bootstrap을 사용하기 위한 코드2
Vue.use(BootstrapVue)

// vue-glide를 사용하기 위한 코드2
Vue.use(VueGlide)

// font-awesome을 사용하기 위한 코드
library.add(faUserSecret)
Vue.component('font-awesome-icon', FontAwesomeIcon)

// vue-lodash 사용하기 위한 코드 1
Vue.use(VueLodash, { name: 'custom' , lodash: lodash })

// Vue.component('star-rating', StarRating)


Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
