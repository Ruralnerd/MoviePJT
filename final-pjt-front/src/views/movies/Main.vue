<template>
  <div class="container w-50 h-75 mt-3">
    <!-- interval 자동으로 슬라이드가 넘어가는 시간 -->
      <b-carousel
        id="carousel-1"
        v-model="slide"
        :interval="2000" 
        label-next=""
        label-prev=""
        controls
        background="#000000"
        img-width="600"
        img-height="600"
        style="text-shadow: 3px 3px 10px #00f;"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
      >
        <MovieCard
          v-for="(movie, idx) in movies"
          :key="idx"
          :movie="movie"  
        />
    </b-carousel>
    <h1>장르별 추천영화</h1>

    <h1>요즘 뜨는 영화</h1>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
<script>
// import axios from 'axios'
// import lodash from 'lodash'
import { mapState } from 'vuex'
import MovieCard from '@/components/movies/MovieCard.vue'

export default {
  name: 'Main',
  components: {
    MovieCard,
  },
  data () {
    return {
      slide: 0,
      sliding: null,
    }
  },
  created: function () {
    this.$store.dispatch('getMovies')
  },
  // mounted: function () {
  //   const movies = _.shuffle([this.movies])
  // },
  computed: {
    // movies: function () {
    //   return this.$store.state.movies
    // },
    ...mapState([
      'movies',
    ])
  },
  methods: {
    onSlideStart() {
      this.sliding = true
    },
    onSlideEnd() {
      this.sliding = false
    },
  },
}
</script>

<style scoped>
* {
  font-family: DungGeunMo;
}
  .test:hover {
    color: lightcoral;
    visibility: hidden;
  }

  .sidebar:hover {
    visibility: visible;
  }

  .carousel-control-next {
    opacity: 1;
    background-color: red;
  }
</style>