<template>
  <div class="">
    <div id="app">
      <div id="nav">
        <router-link to="/">Main</router-link> |
        <router-link to="/recommended">Recommended</router-link> |
        <router-link to="/signup">Sign up</router-link> |
        <router-link to="/signin">Sign in</router-link> |
        <router-link to="/signout">Sign out</router-link> |
        <router-link to="/mymovielist">My Movie List</router-link>
      </div>
      <router-view/>
    </div>
  </div>
</template>


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
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

</style>
