<template>
  <div class="container" style="">
    <div class="d-flex flex-column">
    <h1 class="text-center">리뷰 페이지</h1>
    <!-- <h2>{{movie.id}}</h2> -->
      <ul>
        <Review
          v-for="(review, idx) in reviews"
          :key="idx"
          :review="review"
          @deleteReview="deleteReview"
        />
      </ul>
      <div class="p-1 d-flex align-items-end flex-column">
        <star-rating v-model="star" :star-size="20" :increment="0.5" :show-rating=false class="aa"></star-rating>
        <textarea class="form-control mt-1" placeholder="리뷰" id="floatingReview" v-model="opinion" style="" @keyup.enter="createReview"></textarea>
    </div>
    </div>    
  </div>
</template>

<script>
import axios from 'axios'
import StarRating from 'vue-star-rating'
import Review from '@/components/movies/Review.vue'

export default {
  name: "ReviewList",
  components: {
    Review,
    StarRating
  },
  props: {
    savemovies: {
      type:Object,
    },
    movie: {
      type:Object
    }
  },
  data: function () {
    return {
      reviews: null,
      star: null,
      opinion: null,
    }
  },
  methods: {
    check: function () {
      console.log(this.savemovies)
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getReviews: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/movie_list/${this.savemovies.id}/rates/`,
        headers: this.setToken()
      })
        .then((response) => {
          this.reviews = response.data.reverse()
        })
        .catch((error) => {
          console.log(error)
        })
    },
    createReview: function () {
      const Review = {
        opinion: this.opinion,
        star: this.star*2
      }
      // if (Review.opinion) {
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/movies/movie_list/${this.savemovies.id}/rates/`,
          data: Review,
          headers: this.setToken()
        })
          .then((response) => {
            this.reviews = response.data
            this.getReviews()
            if (this.star*2 >= 7) {
              this.$store.dispatch('rmovie', this.movie)
            }
            this.opinion = null
            this.star = null
            // console.log(this.savemovies.genre_ids)
            
          })
          .catch((error) => {
            console.log(error)
          })
    },
    deleteReview: function (reviewId) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/rates/${reviewId}/`,
        headers: this.setToken()
      })
        .then((response) => {
          console.log(response)
          this.getReviews()
        })
        .catch((error) => {
          console.log(error)
        })
    },
    rmovie: function () {
      this.$store.dispatch('rmovie', this.movie)
    },
  },
  created: function () {
    this.getReviews()
  }
}
</script>

<style>

</style>