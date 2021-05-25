<template>
  <div class="container w-50 h-75">
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
  </div>
</template>

<script>
import axios from 'axios'
import MovieCard from '@/components/movies/MovieCard.vue'

export default {
  name: 'Main',
  components: {
    MovieCard,
  },
  data () {
    return {
      // 영화 담긴 리스트
      movies:[],
      slide: 0,
      sliding: null,
    }
  },
  computed: {
  },
  methods: {
    // 영화 정보를 가져온다
    getMovies () {
      if (this.movies.length === 0) {
        axios.get("https://gist.githubusercontent.com/Ruralnerd/ada51601c3706cf1fe3dc6fe46bd403f/raw/eb3b441c45929b08819713ee6103fe7ad2843d53/movielist.json")
        .then((response) => {
          this.movies=response.data
      })
      } else {
        console.log(this.movies)
      }
    },
    onSlideStart() {
      this.sliding = true
    },
    onSlideEnd() {
      this.sliding = false
    },
  },
  // 데이터 가져오기
  created: function () {
    if (this.movies.length === 0) {
    this.getMovies()
    } else {
      console.log(this.movies)
    }
  },
}
</script>

<style scoped>
/* 
  #sidebar-right {
    display: inline;
  } */

  .test:hover {
    color: lightcoral;
    visibility: hidden;
  }

  .sidebar:hover {
    visibility: visible;
  }
  
  /* .container {
    background-color: red;
  } */
  .carousel-control-next {
    opacity: 1;
    background-color: red;
  }
</style>