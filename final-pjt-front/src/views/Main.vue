<template>
  <div class="container w-75 h-100">
    <h1>Main</h1>
    <!-- interval 자동으로 슬라이드가 넘어가는 시간 -->
      <b-carousel
        id="carousel-1"
        v-model="slide"
        :interval="2000" 
        label-next=""
        label-prev=""
        controls
        indicators
        background="#ababab"
        img-width="500"
        img-height="480"
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
import MovieCard from '@/components/MovieCard.vue'
// import MovieDetail from '@/components/MovieDetail.vue'
// import ModalView from '@/components/ModalView.vue'
// import { Glide, GlideSlide } from 'vue-glide-js'

export default {
  name: 'Main',
  components: {
    MovieCard,
    // MovieDetail,
    // ModalView
    // [Glide.name]: Glide,
    // [GlideSlide.name]: GlideSlide
  },
  data () {
    return {
      // 영화 담긴 리스트
      movies:[],
      // 캐러솔 data
      slide: 0,
      sliding: null,
      // 모달을 위한 코드
      // modalShow: false,
      // uid: '',
    }
  },
  computed: {

  },
  methods: {
    // 영화 정보를 가져온다
    getMovies () {
      axios.get("https://gist.githubusercontent.com/Ruralnerd/ada51601c3706cf1fe3dc6fe46bd403f/raw/bc9dd8ea781942b31e4380f394a321bee65a1949/movietest.json")
      .then((response) => {
        this.movies=response.data
      })
    },
    // 캐러솔 슬라이드 start, end
    onSlideStart() {
      this.sliding = true
      // console.log(slide)
      
    },
    onSlideEnd() {
      this.sliding = false
      // console.log(slide)
    },
  },
  // 데이터 가져오기
  created: function () {
    this.getMovies()
  },
}
</script>
