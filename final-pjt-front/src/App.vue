<template>
    <div class="bg">
      <div class="container">
        <div id="app" class="">
          <div id="nav" class="">
            <b-navbar type="light" variant="dark">
              <b-navbar-nav>
                <router-link :to="{ name: 'Main' }" class="text-decoration-none p-2 ps-3">Main</router-link>
                <router-link v-if="isSignin" :to="{ name: 'RecommendedMovieList' }" class="text-decoration-none p-2">Recommended</router-link>
                <router-link v-if="isSignin" :to="{ name: 'MyMovieList' }" class="text-decoration-none p-2">My Movie List</router-link>
                <router-link :to="{ name: 'Community' }" class="text-decoration-none p-2">Community</router-link>
              </b-navbar-nav>

              <b-navbar-nav class="ml-auto">
                <!-- <b-nav-form>
                  <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
                  <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
                </b-nav-form> -->

                <b-nav-item-dropdown right>
                  <template #button-content>
                    <span class="p-2">User</span>
                  </template>
                  <span v-if="isSignin"><b-dropdown-item :to="{ name: 'Signout' }" class="text-decoration-none" @click.native="signout">Sign out</b-dropdown-item></span>
                  <span v-else>
                    <b-dropdown-item :to="{ name: 'Signup' }" class="text-decoration-none">Sign up</b-dropdown-item>
                    <b-dropdown-item :to="{ name: 'Signin' }" class="text-decoration-none">Sign in</b-dropdown-item>
                  </span>
                </b-nav-item-dropdown>
              </b-navbar-nav>
            </b-navbar>
          </div>
          <router-view @signin="isSignin=true"/>
        </div>
      </div>
    </div>
</template>


<script>
export default {
  name: 'App',
  data: function () {
    return {
      isSignin: false,
    }
  },
  methods: {
    signout: function () {
      this.isSignin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Signin' })
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
  /* margin-left: 200px; */
  /* margin-right: 200px; */
}

#nav {
  padding-top: 30px;
}

#nav a {
  font-weight: bold;
  /* color: #2c3e50; */
  color: darksalmon;
  
}

#nav a.router-link-exact-active {
  color: #42b983;
}
.bg {
  min-height: 100vh;
  /* height: 1000px; */
  /* width: 1870px; */
  /* background-size: initial; */
  /* background-color: black; */
  background-image: url("https://i.ibb.co/5hrws9R/1330852.jpg");
  /* background-size: 100%; */
  background-repeat: repeat;
  /* background-position: center; */
}


</style>
