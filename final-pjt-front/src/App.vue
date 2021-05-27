<template>
  <div class="bg">
    <div class="">
      <div id="app" class="">
        <div id="nav" class="" v-if='$route.name !== "Cover"'>
          <b-navbar type="light" variant="" style="background-color:#4B0082">
            <b-navbar-nav>
              <router-link v-if="isSignin" :to="{ name: 'Main' }" class="text-decoration-none p-2 px-4">메인</router-link>
              <router-link v-if="isSignin" :to="{ name: 'RecommendedMovieList' }" class="text-decoration-none p-2 px-4">추천영화</router-link>
              <router-link v-if="isSignin" :to="{ name: 'YoutubeSearch' }" class="text-decoration-none p-2 px-4">최신기술</router-link>
              <router-link v-if="isSignin" :to="{ name: 'Community' }" class="text-decoration-none p-2 px-4">게시판</router-link>
              <router-link v-if="isSignin" :to="{ name: 'Search' }" class="text-decoration-none p-2 px-4">검색결과</router-link>
            </b-navbar-nav>
            <!-- <div class='box1 mm'> -->
              <b-navbar-nav class="mm">
                <b-nav-form class="d-flex align-items-center">
                  <div class="search-input" v-if="isSignin">
                    <b-form-input size="sm" class="mr-sm-2" placeholder="Search" v-model="inputText" @keydown.enter.prevent="getSearch"></b-form-input>
                  </div>
                  <div class="search-button" v-if="isSignin">
                    <button size="sm" class="my-2 my-sm-0 ms-1" type="button" @click="getSearch">Search</button>
                  </div>
                </b-nav-form>

                <b-nav-item-dropdown right>
                  <template #button-content>
                    <span class="p-2 px-4">회원</span>
                  </template>
                  <span v-if="isSignin"><b-dropdown-item class="text-decoration-none" @click.native="signout">로그-아웃</b-dropdown-item></span>
                  <span v-else>
                    <b-dropdown-item :to="{ name: 'Signup' }" class="text-decoration-none">회원가입</b-dropdown-item>
                    <b-dropdown-item :to="{ name: 'Signin' }" class="text-decoration-none">로그-인</b-dropdown-item>
                  </span>
                </b-nav-item-dropdown>
              </b-navbar-nav>
            <!-- </div> -->
          </b-navbar>
        </div>
        <router-view @signin="isSignin=true"/>
      </div>
    </div>
  <div class="container" v-if='$route.name === "Search"'>
    <h1>Recommended Movie List</h1>
      <div class="row row-cols-3 row-cols-md-3 g-3">
        <Search
          v-for="(result, idx) in ans"
          :key="idx"
          :result="result"
        />
      </div>      
  </div>
  </div>
</template>


<script>
import axios from 'axios'
import Search from '@/views/movies/Search.vue'

export default {
  name: 'App',
  components: {
    Search
  },
  data: function () {
    return {
      isSignin: false,
      ans: [],
      inputText: null,
    }
  },
  methods: {
    signout: function () {
      this.isSignin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Signin' })
    },
    getSearch: function () {
      // const params = {
      //   q: this.inputText
      //   }

      axios({
        method: 'get',
        // url: `http://127.0.0.1:8000/movies/search`,
        url: `https://api.themoviedb.org/3/search/movie?api_key=1850c79236f1a6c5846dc306a959dc25&language=ko-KR&query=${this.inputText}&page=1&include_adult=false`,
        // params
        // headers: this.setToken()
      })
        .then((response) => {
          this.ans = response.data['results']
          // console.log(response)
          // console.log(response.data)
          this.inputText = ''
          this.$router.push({ name: 'Search' })
        })
        .catch((error) => {
          console.log(error)
        })
    }    
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isSignin = true
    }
  }
}
</script>

<style>
@font-face {
  font-family: DungGeunMo;
  src:url("C:/Users/leeww/Desktop/SSAFY/insertO/my projects/final-pjt/DungGeunMo/DungGeunMo.eot");
  src:url("C:/Users/leeww/Desktop/SSAFY/insertO/my projects/final-pjt/DungGeunMo/DungGeunMo.woff");
  src:url("C:/Users/leeww/Desktop/SSAFY/insertO/my projects/final-pjt/DungGeunMo/DungGeunMo.woff2");

}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  /* padding-top: 30px; */
  /* position: sticky; */
}

#nav a {
  font-weight: bold;
  color:yellow;
  
}

#nav a.router-link-exact-active {
  color: blue;
}
.bg {
  min-height: 120vh;
  background-image: url("https://i.ibb.co/5hrws9R/1330852.jpg");
  background-repeat: repeat;
}

.nav-item > .show {
  background-color:black;
}

.search-input {
  /* border: 2px solid red; */
  float: left;
}

.search-button {
  /* border:5px solid yellow; */
  float: right;
  
}

.mm {
  margin-left: auto;
}
.my-sm-0 {
  position: relative;
  /* margin-top: -60px; */
}
</style>
