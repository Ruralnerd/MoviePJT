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
    <div class="p-1 d-flex align-items-end">
      <textarea class="form-control" placeholder="리뷰" id="floatingReview" v-model="content" style="" @keyup.enter="createReview"></textarea>
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
  data: function () {
    return {
      reviews: null,
      content: null,
    }
  },
  methods: {
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
        url: '#',
        headers: this.setToken()
      })
        .then((response) => {
          this.reviews = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    
  }
}
</script>

<style>

</style>