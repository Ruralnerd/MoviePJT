<template>
  <div class='d-flex flex-column review-lh'>
    <p class="" style="color:skyblue">{{ review.username }}</p><p class="ca-pos" style>{{review.created_at}}</p>
    <p class="ovfl boxjam star-pos" style="color:yellow">{{ review.star }}점</p><p class="boxjam ms-4">{{ review.opinion }}</p><div class='as boxjam'><button v-if='myinfo.username===review.username' type="button" class="ms-2" style="" @click="deleteReview">x</button></div>
  </div>
</template>

<script>
// import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'Review',
  props: {
    review: {
      type:[Object,Number,String]
    }
  },
  computed: {
    ...mapState([
      'myinfo',
    ])
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
      this.$emit('deleteReview', this.review.id)
      // axios({
      //   method: 'delete',
      //   url: `http://127.0.0.1:8000/movies/rates/${this.review.id}/`,
      //   headers: this.setToken()
      // })
      //   .then((response) => {
      //     console.log(response)
      //   })
      //   .catch((error) => {
      //     console.log(error)
      //   })
    },
  }
}
</script>

<style>

  .ovfl {
    overflow: hidden;
    text-overflow: ellipsis;
    /* display: -webkit-box; */
    white-space: nowrap;
    /* -webkit-line-clamp: 16;    라인수 */
    /* -webkit-box-orient: vertical; */
    /* word-wrap:break-word; */
    /* line-height: 1.8rem; */
    height: 50;
    width:200px;
  }

  .as {
    position: absolute;
    margin-top: 28px;
    margin-left: 200px;
  }

  .review-lh {
    line-height: 15px;
  }

  .ca-pos {
    position: absolute;
    margin-left: 80px;
    font-size: 12px;
  }

  .star-pos {
  position: absolute;
  font-size: 12px;  
  margin-top: 30px;
  }

</style>