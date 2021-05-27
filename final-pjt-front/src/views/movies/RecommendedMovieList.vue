<template>
  <div class="container">
    <h1>Recommended Movie List</h1>
    <div class="row row-cols-3 row-cols-md-3 g-3">
      <RecommendedMovie
        v-for="(recommend, idx) in recommends"
        :key="idx"
        :recommend="recommend"  
      />
      
    </div>      
  </div>
</template>

<script>
import axios from 'axios'
import RecommendedMovie from '@/components/movies/RecommendedMovie.vue'


export default {
  name: 'RecommendedMovieList',
  components: {
    RecommendedMovie,
  },
  data: function() {
    return {
      recommends:[],
    }
  },
  computed: {
    savemovies: function () {
      return this.$store.state.savemovies
    },
  },
  methods: {
    getRecommend: function () {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.savemovies.id}/recommendations?api_key=1850c79236f1a6c5846dc306a959dc25&language=ko-KR&page=1`,
      })
        .then((response) => {
          this.recommends = response.data['results']
          console.log(this.recommends)
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
  created: function () {
    this.getRecommend()
  },
}
</script>

<style>

</style>