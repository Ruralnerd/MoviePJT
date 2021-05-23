<template>
  <div>
    <!-- <h1>{{ mymovie.title }}</h1> -->
    <!-- variable routing이 가능할까? -->
    <!-- <h1><router-link :to="mymovie.id">{{ mymovie.title }}</router-link></h1> -->
    <h2 @click="[saveId(), modalShow=!modalShow]">{{ mymovie.title }}</h2>
    <!-- <button @click="[saveId(), modalShow=!modalShow]">눌러봥</button> -->
    <b-modal id="modal-lg" size="lg" v-model="modalShow">
      <div class="d-flex">
        <img :src="'https://image.tmdb.org/t/p/w300/'+ savemovies[0].poster_path" alt="">
        <div class="w-25">
          <p>개봉일 {{ savemovies[0].release_date }}</p>
          <p>평점 {{ savemovies[0].vote_average }}</p>
          <p>상영시간 {{ savemovies[0].runtime }}분</p>
        </div>
        <Review/>
      </div>
    </b-modal>
  </div>
</template>

<script>
import Review from '@/components/movies/Review.vue'

export default {
  name: 'MyMovie',
  components: {
    Review
  },
  data() {
    return {
      modalShow: false,
    }
  },
  props: {
    mymovie: {
      type: Object,
    }
  },
  methods: {
    saveId: function () {
      this.$store.dispatch('saveId', this.mymovie)
    },
  },
  computed: {
    savemovies: function () {
      return this.$store.state.savemovies
    }
  }
}
</script>

<style>

</style>