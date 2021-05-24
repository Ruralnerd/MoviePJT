<template>
  <div class="container d-flex" style="">
    <div class="justify-content-start">
      <p class="bg-danger">제목 : {{ detail.title }}</p>
      <p>영화 : {{ detail.movie_title }}</p>
      <p>본문 : {{ detail.content }}</p>
      <hr>
      <p>댓글</p>
      <Comment
        v-for="(comment, idx) in comments"
        :key="idx"
        :comment="comment"
      />
      <div class="p-1">
        <textarea class="form-control" placeholder="댓글" id="floatingContent" v-model="content" style="" @keyup.enter="createComment"></textarea>
      </div>
    </div>
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
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getDetail: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/community/review/${this.id}`,
        headers: this.setToken()
      })
        .then((response) => {
          this.detail = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getComments () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/community/review/${this.id}/comments/`,
        headers: this.setToken()
      })
        .then((response) => {
          this.comments = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    createComment: function () {
      const Comment = {
        content: this.content
      }
      if (Comment.content) {
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/api/community/review/${this.detail.id}/comments/`,
          data: Comment,
          headers: this.setToken()
        })
          .then((response) => {
            console.log(response)
            this.$router.push({ name: 'ArticleDetail', params: {id:`${this.detail.id}`} })
          })
          .catch((error) => {
            console.log(error)
          })
      }
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
  .rr {
    margin-left: 300px;
  }

</style>