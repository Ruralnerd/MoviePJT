<template>
  <div>
    <p>{{ review.star }}점  {{ review.opinion }}<button type="button" class="ms-2" style="" @click="deleteReview">x</button></p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Review',
  props: {
    review: {
      type:Object
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
    deleteReview: function () {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/rates/${this.review.id}/`,
        headers: this.setToken()
      })
        .then((response) => {
          console.log(response)
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