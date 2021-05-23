<template>
  <div>
    <h1>MyMovieList</h1>
    <MyMovie v-for="(mymovie, idx) in mymovies" :key="idx" :mymovie="mymovie"/>
  </div>
</template>

<script>
import MyMovie from '@/components/movies/MyMovie.vue'

export default {
  name: "MyMovieList",
  components: {
    MyMovie
  },
  computed: {
    mymovies: function () {
      return this.$store.state.mymovies
    },
  }
}
</script>

<style>

</style>