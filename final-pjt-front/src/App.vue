<template>
  <div class="zz">
    <div id="app" class="container">
      <div id="nav">
        <b-navbar type="light" variant="dark">
          <b-navbar-nav>
            <router-link :to="{ name: 'Main' }" class="text-decoration-none p-2">Main</router-link>
            <router-link :to="{ name: 'Recommended' }" class="text-decoration-none p-2">Recommended</router-link>
            <!-- <router-link :to="{ name: 'Signup' }">Sign up</router-link> -->
            <!-- <router-link :to="{ name: 'Signin' }">Sign in</router-link> -->
            <!-- <router-link :to="{ name: 'Signout' }">Sign out</router-link> -->
            <router-link :to="{ name: 'MyMovieList' }" class="text-decoration-none p-2">My Movie List</router-link>
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
              <b-dropdown-item><router-link :to="{ name: 'Signup' }" class="text-decoration-none">Sign up</router-link></b-dropdown-item>
              <b-dropdown-item><router-link :to="{ name: 'Signin' }" class="text-decoration-none">Sign in</router-link></b-dropdown-item>
              <b-dropdown-item><router-link :to="{ name: 'Signout' }" class="text-decoration-none" @click.native="signout">Sign out</router-link></b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-navbar>
      </div>
      <router-view @login="isSignin=true"/>
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  /* color: #2c3e50; */
  color: darksalmon;
  
}

#nav a.router-link-exact-active {
  color: #42b983;
}
.zz {
  background-color: black;
  background-image: url("https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FudBi1%2FbtqDTjGXEpp%2FNgyg3Mjks6TNIKvK8kTLa0%2Fimg.jpg");
  background-size: 100%;
  background-repeat: no-repeat;
  background-position: center;
}
</style>
