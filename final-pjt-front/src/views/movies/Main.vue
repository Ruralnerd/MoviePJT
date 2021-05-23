<template>
  <div class="container w-50 h-75">
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
    <!-- <div class="">
      <button class="sidebar">zz</button>
      <b-sidebar class="">
        <div class="px-3 py-2">
          <p>
            Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis
            in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.
          </p>
          <b-img src="https://picsum.photos/500/500/?image=54" fluid thumbnail></b-img>
        </div>
      </b-sidebar>
    </div> -->
    
    <!-- <p class="test">asdasd</p> -->

    <!-- <b-button @mouseover="handleHover()">이걸로 이벤트를</b-button>
    <div v-if="isHovered" class="d-flex flex-row-reverse">
      <p>보였다</p>
    </div>
    <p v-else>안보였다</p> -->
  </div>
</template>

<script>
import axios from 'axios'
import MovieCard from '@/components/movies/MovieCard.vue'
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
      // isHovered: false
    }
  },
  computed: {

  },
  methods: {
    // 영화 정보를 가져온다
    getMovies () {
      // axios.get("https://gist.githubusercontent.com/Ruralnerd/ada51601c3706cf1fe3dc6fe46bd403f/raw/bc9dd8ea781942b31e4380f394a321bee65a1949/movietest.json")
      axios.get("https://gist.githubusercontent.com/Ruralnerd/ada51601c3706cf1fe3dc6fe46bd403f/raw/eb3b441c45929b08819713ee6103fe7ad2843d53/movielist.json")
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

    // 사이드바 호버
    // hoverHandler(isHovered) {
    //   if (isHovered) {
    //     console.log('올라왔다')

    //   } else {
    //     console.log('내려왔다')
    //   }
    // }
    handleHover() {
      this.isHovered = !this.isHovered
    }
  },
  // 데이터 가져오기
  created: function () {
    this.getMovies()
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
</style>