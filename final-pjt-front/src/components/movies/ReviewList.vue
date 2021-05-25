<template>
  <div>
    <h1>Review List Page</h1>
    <ul>
      <Review
        v-for="(review, idx) in reviews"
        :key="idx"
        :review="review"
      />
    </ul>
    <!-- <button @click="getReviews"></button> -->
    <div class="p-1 d-flex align-items-end">
      <textarea class="form-control" placeholder="별점" id="floatingReview" v-model="star" style="" @keyup.enter="createReview"></textarea>
      <textarea class="form-control" placeholder="리뷰" id="floatingReview" v-model="opinion" style="" @keyup.enter="createReview"></textarea>
    </div>    
  </div>
</template>

<script>
import axios from 'axios'
import Review from '@/components/movies/Review.vue'

export default {
  name: "ReviewList",
  components: {
    Review
  },
  props: {
    savemovies: {
      type:Object,
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
          this.reviews = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    createReview: function () {
      const Review = {
        opinion: this.opinion,
        star: this.star
      }
      if (Review.opinion) {
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/movies/movie_list/${this.savemovies.id}/rates/`,
          data: Review,
          headers: this.setToken()
        })
          .then((response) => {
            this.reviews = response.data
            this.getReviews()
          })
          .catch((error) => {
            console.log(error)
          })
      }
    } 
  },
  created: function () {
    this.getReviews()
  }
}
</script>

<style>

</style>