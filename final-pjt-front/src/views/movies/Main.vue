<template>
  <div class="cc">
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
          style="text-shadow: 3px 3px 10px #ff4500;"
          @sliding-start="onSlideStart"
          @sliding-end="onSlideEnd"
        >
          <MovieCard
            v-for="(movie, idx) in movies"
            :key="idx"
            :movie="movie"  
          />
      </b-carousel>
    </div>
    <div class="container w-75 h-50 gld">
      <h1>최신 영화</h1>
        <div>
          <vue-glide
            :perView=4
            :gap=20
            :autoplay=2345
            :bound=true
            :keyboard=false
          >
            <vue-glide-slide
              v-for="(latestmovie, idx) in latestmovies"
              :key="idx"
              style="width:600px"          
            >
              <LatestMovie :latestmovie="latestmovie"/>
            </vue-glide-slide>
          </vue-glide>
        </div>    
      <h1>요즘 뜨는 영화</h1>
        <div>
          <vue-glide
            :perView=4
            :gap=20
            :autoplay=3456
            :bound=true
            :keyboard=false
          >
            <vue-glide-slide
              v-for="(popularmovie, idx) in popularmovies"
              :key="idx"
              style=""          
            >
              <PopularMovie :popularmovie="popularmovie"/>
            </vue-glide-slide>
          </vue-glide>
        </div>
      <h1>오늘의 영화</h1>
        <div>
          <vue-glide
            :perView=4
            :gap=20
            :autoplay=5678
            :bound=true
            :keyboard=false
          >
            <vue-glide-slide
              v-for="(todaymovie, idx) in todaymovies"
              :key="idx"
              style="width:600px"          
            >
              <TodayMovie :todaymovie="todaymovie"/>
            </vue-glide-slide>
          </vue-glide>
        </div>
    </div>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
<script>
// import axios from 'axios'
// import lodash from 'lodash'
import { Glide, GlideSlide } from 'vue-glide-js'
import { mapState } from 'vuex'
import MovieCard from '@/components/movies/MovieCard.vue'
import LatestMovie from '@/components/movies/LatestMovie.vue'
import PopularMovie from '@/components/movies/PopularMovie.vue'
import TodayMovie from '@/components/movies/TodayMovie.vue'

export default {
  name: 'Main',
  components: {
    MovieCard,
    LatestMovie,
    PopularMovie,
    TodayMovie,
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide    
  },
  data () {
    return {
      slide: 0,
      sliding: null,
    }
  },
  created: function () {
    this.$store.dispatch('getMovies')
    this.$store.dispatch('getLatest')
    this.$store.dispatch('getPopular')
    this.$store.dispatch('getToday')
  },
  computed: {
    // movies: function () {
    //   return this.$store.state.movies
    // },
    ...mapState([
      'movies',
      'latestmovies',
      'popularmovies',
      'todaymovies',
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

  .carousel-control-next {
    opacity: 1;
    background-color: red;
    color:red;
  }

  .gld h1 {
    color: yellow;
    text-align: start;
  }
</style>