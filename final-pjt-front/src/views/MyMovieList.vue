<template>
  <div>
    <h1>MyMovieList</h1>
    <MyList v-for="(mymovie, idx) in mymovies" :key="idx" :mymovie="mymovie"/>
  </div>
</template>

<script>
import MyList from '@/components/MyList.vue'

export default {
  name: "MyMovieList",
  components: {
    MyList
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