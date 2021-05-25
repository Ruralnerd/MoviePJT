<template>
  <div class="container">
      <div class="carousel-item p-0 img_wrap">
        <img :src="'https://image.tmdb.org/t/p/w400/'+ movie.poster_path" class="image-fluid hv" style="height:700px; width:500px" alt="..." @click="[saveId(), modalShow=!modalShow]">
        <div class="container d-flex">
          <p class="overview">
            제목 {{ movie.title }}
            평점 {{ movie.vote_average }}
          개봉일 {{ movie.release_date }}</p>
          <!-- <p class="overview">평점 {{ movie.vote_average }}</p>
          <p class="overview">개봉일 {{ movie.release_date }}</p> -->
          <!-- <p class="overview">{{ movie.overview }}</p> -->
        </div>
        <b-button @click="saveMovie" class="bt">☆</b-button>
      </div>
    <!-- <b-button @click="[modalShow=!modalShow, saveId()]">이거임</b-button> -->
    <b-modal id="modal-xl" size="xl" v-model="modalShow" :title=savemovies[0].title class="">
      <div class="d-flex">
        <img :src="'https://image.tmdb.org/t/p/w400/'+ savemovies[0].poster_path" alt="" class="poster">
        <p class="overview1" style="width:400px">{{ savemovies[0].overview }}</p>
        <div class="w-25 d-flex flex-column p-3">
          <p> 개봉일 {{ savemovies[0].release_date }}</p>
          <p> 평점 {{ savemovies[0].vote_average }}</p>
        </div>
        <ReviewList/>
      </div>
    </b-modal>

  </div>
</template>


<script>
// import MovieDetail from '@/components/MovieDetail.vue'
import ReviewList from '@/components/movies/ReviewList.vue'

export default {
  name: 'MovieCard',
  components: {
    // MovieDetail,
    ReviewList
  },
  data() {
    return {
      modalShow: false,
    }
  },
  props: {
    movie: {
      type: Object,
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
  // created: function () {
  //   this.$store.dispatch('saveTitle')
  // },
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
  
  .close {
    visibility: hidden;

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
  
  .overview {
    position: absolute;
    margin-top: -200px;
    visibility: hidden;
    opacity: 0;
  }

  .img_wrap:hover .overview {
    visibility: visible;
    opacity: 1;
  }
  
  .hv:hover {
    opacity: 0.5;
  }

  .bt {
    position: relative;
    padding-right: 200px;
  }
</style>