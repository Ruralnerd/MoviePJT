<template>
  <div class="">
      <div class="carousel-item p-0 img_wrap" style="">
        <img :src="'https://image.tmdb.org/t/p/w400/'+ movie.poster_path" class="image-fluid hv" style="height:700px; width:500px" alt="..." @click="[saveId(), modalShow=!modalShow]">
        <div class="container d-flex flex-column">
          <p class="overview">개봉일 {{ movie.release_date }}</p>
          <p class="overview">평점 {{ movie.vote_average }}</p>
          <p class="overview">{{ movie.title }}</p>
        </div>
      </div>
    <b-modal id="modal-lg" size="lg" v-model="modalShow" :title=movie.title class="">
      <div class="d-flex">
        <div class="img_wrap1 hv-1">
          <img :src="'https://image.tmdb.org/t/p/w400/'+ movie.poster_path" alt="" class="hv1">
          <p class="overview1" style="width:400px">{{ movie.overview }}</p>
        </div>
        <div class='ms-4' style="flex:1;">
          <ReviewList
            :savemovies="savemovies"
          />
        </div>
      </div>
    </b-modal>
  <!-- 왼쪽이 데이터 오른쪽이 이름 -->
  </div>
</template>


<script>
import ReviewList from '@/components/movies/ReviewList.vue'

export default {
  name: 'MovieCard',
  components: {
    ReviewList
  },
  data() {
    return {
      modalShow: false,
    }
  },
  props: {
    movie: {
      type: Object
    },
  },
  methods: {
    check() {
      console.log(this.savetitle)
    },
    saveMovie: function () {
      const smovie = this.movie
      this.$store.dispatch('saveMovie', smovie)
    },
    saveId: function () {
      this.$store.dispatch('saveId', this.movie)
    },
  },
  computed: {
    recommendMovie: function () {
      return this.$store.getters.recommendMovie
    },
    savemovies: function () {
      return this.$store.state.savemovies
    },
    savetitle: function () {
      return this.$store.state.savetitle
    }
  },
}
</script>

<style>
  .pos {
    margin-left: 210px;
    margin-bottom: 100px;
    position: absolute;

  }
  .modal-body {
    background-color: black;
  }

  .modal-header {
    background-color: black;
  }

  .modal-header *{
    color:yellow
  }

  .modal-header .close{
    color:black
  }

  h5 {
    color: white;
  }

  p {
    color: white;
  }

  .modal-footer {
    background-color: black;
  }
  
  .modal-footer button {
    background-color: blue;
    font-size: 20px;
    visibility: hidden;
  }
  .overview {
    position: relative;
    margin-top: -200px;
    visibility: hidden;
    opacity: 0;
    font-size: 40px;
    color: gold;
  }

  .img_wrap:hover .overview {
    visibility: visible;
    opacity: 1;
  }
  
  .hv:hover {
    opacity: 0.5;
  }

  .overview {
    position: relative;
    margin-top: -200px;
    visibility: hidden;
    opacity: 0;
    font-size: 40px;
  }



  .img_wrap1:hover .overview1 {
    visibility: visible;
    opacity: 1;
  }
  
  .hv1:hover {
    opacity: 0.5;
  }

  .overview1 {
    margin-top: -550px;
    position: absolute;
    visibility: hidden;
    opacity: 0;
    font-size: 20px;
    padding:20px;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 16;    /* 라인수 */
    -webkit-box-orient: vertical;
    word-wrap:break-word;
    line-height: 1.8rem;
    height: 470px;
  }


  .bt {
    position: relative;
    padding-right: 200px;
  }

  #carousel-1 > .carousel-control-next {
    opacity: 1;
    /* background-color: rgba( 255, 255, 255, 0.5 ); */
    background-color: black;
    color:red;
    /* visibility: hidden; */
    /* opacity: 0; */
  }

  #carousel-1 >  .carousel-control-prev {
    opacity: 1;
    /* background-color: rgba( 255, 255, 255, 0.5 ); */
    background-color: black;
    color:red;
    /* visibility: hidden; */
    /* opacity: 0; */
  }
</style>