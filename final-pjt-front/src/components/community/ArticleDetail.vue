<template>
  <div class="container">
    <h1>ArticleDetail</h1>
    <p>제목 : {{ detail.title }}</p>
    <p>영화 : {{ detail.movie_title }}</p>
    <p>본문 : {{ detail.content }}</p>
    
    <Comment
      v-for="(comment, idx) in comments"
      :key="idx"
      :comment="comment"
    />
    <button @click="check">click</button>
    <!-- <CommentForm/> -->
    <b-form-textarea
      id="textarea-rows"
      placeholder=""
      rows="2"
      class="col-sm-1 col-lg-2"
      v-model="content"
      @keyup.enter="check"
    ></b-form-textarea>
  </div>
</template>

<script>
import axios from 'axios'
import Comment from '@/components/community/Comment.vue'
// import CommentForm from '@/components/community/CommentForm.vue'


export default {
  name:'ArticleDetail',
  components: {
    Comment,
    // CommentForm,
  },
  data () {
    return {
      detail:[],
      comments:[],
      content:'',
    }
  },
  props: {
    id: {
      type:[Number, String],
    },
  },
  methods: {
    getDetail: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/community/review/${this.id}`,
        // url: `http://127.0.0.1:8000/api/community/review/1`,
        // headers: this.setToken()
      })
        .then((response) => {
          this.detail = response.data
          // console.log(this.detail)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getComments () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/community/review/${this.id}/comments/`,
        // headers?
      })
        .then((response) => {
          this.comments = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    check () {
      console.log(this.detail)
    }
  },
  created: function () {
    this.getDetail()
    this.getComments()
  },
}
</script>

<style>

</style>