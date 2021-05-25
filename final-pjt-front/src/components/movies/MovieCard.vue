<template>
  <div class="container">
      <div class="carousel-item p-0">
        <img :src="'https://image.tmdb.org/t/p/w400/'+ movie.poster_path" class="image-fluid" style="height:700px; width:500px" alt="..." @click="[saveId(), modalShow=!modalShow]">
        <p>{{ movie.title }}</p>
        <b-button @click="saveMovie" class="bt">☆</b-button>
      </div>
    <!-- <b-button @click="[modalShow=!modalShow, saveId()]">이거임</b-button> -->
    <b-modal id="modal-xl" size="xl" v-model="modalShow" :title=savemovies[0].title class="">
      <div class="d-flex">
        <img :src="'https://image.tmdb.org/t/p/w400/'+ savemovies[0].poster_path" alt="" class="poster">
        <p class="overview" style="width:400px">{{ savemovies[0].overview }}</p>
        <div class="w-25 d-flex flex-column p-3">
          <p> 개봉일 {{ savemovies[0].release_date }}</p>
          <p> 평점 {{ savemovies[0].vote_average }}</p>
          <p> 상영시간 {{ savemovies[0].runtime }}분</p>
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
  }

  .bt {
    position: relative;
    padding-right: 200px;
  }
</style>