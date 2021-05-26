<template>
  <div class="container col-sm-6" style="">
    <div class="d-flex flex-column justify-content-start">
      <p class="text-start">제목 : {{ detail.title }}</p>
      <p class="text-start">영화 : {{ detail.movie_title }}</p>
      <p class="text-start">{{ detail.content }}</p>
      <div class="d-flex justify-content-end">
        <button type="button" class="" @click="goUpdate">수정</button>
        <button type="button" class="ms-1" @click="deleteDetail">삭제</button>
      </div>
      <hr>
      <p class="text-start">댓글</p>
      <Comment
        v-for="(comment, idx) in comments"
        :key="idx"
        :comment="comment"
        :detail="detail"
      />
      <!-- <Comment :detail="detail"/> -->
      <div class="p-1">
        <textarea class="form-control" placeholder="댓글" id="floatingContent" v-model="content" style="" @keyup.enter="createComment"></textarea>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Comment from '@/components/community/Comment.vue'


export default {
  name:'ArticleDetail',
  components: {
    Comment,
  },
  data () {
    return {
      detail:[],
      comments:[],
      content:null,
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
        url: `http://127.0.0.1:8000/community/review/${this.id}`,
        headers: this.setToken()
      })
        .then((response) => {
          this.detail = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    goUpdate: function () {
      this.$router.push({ name: 'ArticleUpdateForm' })
    },
    deleteDetail: function () {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/community/review/${this.detail.id}/`,
        headers: this.setToken()
      })
        .then((response) => {
          console.log(response)
          // 글 삭제가 완료되면 게시판으로 보내자
          this.$router.push({ name: 'Community' })
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getComments () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/review/${this.id}/comments/`,
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
          url: `http://127.0.0.1:8000/community/review/${this.detail.id}/comments/`,
          data: Comment,
          headers: this.setToken()
        })
          .then((response) => {
            console.log(response)
            this.getComments()
            // 댓글을 작성했으면 댓글창을 초기화하는 코드가 있어야함
            this.content = null
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
  
  .bgc {
    background-color:blue
  }

</style>