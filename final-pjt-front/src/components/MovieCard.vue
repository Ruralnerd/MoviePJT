<template>
  <div class="container">
    <b-carousel-slide>
      <template #img>
        <img class="" :src="'https://image.tmdb.org/t/p/w300/'+ movie.poster_path" width="600" height="700" @click="[saveId(), modalShow=!modalShow]">
      </template>
      <h1>{{ movie.title }}</h1>
      <b-button @click="saveMovie" class="btn btn-primary">☆</b-button>
    </b-carousel-slide>
    <!-- <b-button @click="[modalShow=!modalShow, saveId()]">이거임</b-button> -->
    <b-modal id="modal-lg" size="lg" v-model="modalShow" :title= savemovies[0].title class="bgc">
      <div class="d-flex">
        <img :src="'https://image.tmdb.org/t/p/w300/'+ savemovies[0].poster_path" alt="">
        <div class="w-25">
          <p>개봉일 {{ savemovies[0].release_date }}</p>
          <p>평점 {{ savemovies[0].vote_average }}</p>
          <p>상영시간 {{ savemovies[0].runtime }}분</p>
        </div>
        <Review/>
      </div>
      <!-- <p class="my-4">{{ savemovies[0].title }}</p> -->
    </b-modal>
  </div>
</template>


<script>
// import MovieDetail from '@/components/MovieDetail.vue'
import Review from '@/components/Review.vue'

export default {
  name: 'MovieCard',
  components: {
    // MovieDetail,
    Review
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
    background-color: gray;
  }

  .modal-header {
    background-color: khaki;
  }
  
  .close {
    visibility: hidden;

  }

  .close::after {
    /* content:'X'; */
    /* display: block; */
    visibility: visible;
    /* position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0; */
  }
  /* .btn-secondary {
    visibility: hidden;
  } */
  /* .btn-secondary:after {
    content: '닫기';
    background-color: chartreuse;
    visibility: visible;
  } */
</style>