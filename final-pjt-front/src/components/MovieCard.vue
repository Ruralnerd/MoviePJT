<template>
  <div class="container">
    <b-carousel-slide>
      <template #img>
        <img class="" :src="'https://image.tmdb.org/t/p/w300/'+ movie.poster_path" width="400" height="600" @click="[saveId(), modalShow=!modalShow]">
      </template>
      <h1>{{ movie.title }}</h1>
      <b-button @click="saveMovie" class="">☆</b-button>
    </b-carousel-slide>
    <!-- <b-button @click="[modalShow=!modalShow, saveId()]">이거임</b-button> -->
    <b-modal v-model="modalShow">
      <!-- <MovieDetail/> -->
    </b-modal>
  </div>
</template>


<script>
import MovieDetail from '@/components/MovieDetail.vue'

export default {
  name: 'MovieCard',
  conponents: {
    MovieDetail,
  },
  data() {
    return {
      modalShow: false,
      uid: [],
    }
  },
  props: {
    movie: {
      type: Object,
    },
    // uid
  },
  methods: {
    saveMovie: function () {
      const smovie = this.movie
      this.$store.dispatch('saveMovie', smovie)
    },
    saveId: function () {
      // const uid = this.movie.id
      this.uid.push(this.movie.id)
      // console.log(this.movie.id)
    }
  },
  computed: {
    recommendMovie: function () {
      return this.$store.getters.recommendMovie
    },
  },
}
</script>

<style>
  .pos {
    margin-left: 210px;
    margin-bottom: 100px;
    position: absolute;

  }

</style>