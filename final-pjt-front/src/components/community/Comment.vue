<template>
  <div class="d-flex">
    <p class="text-start">{{ comment.content }} {{comment.created_at}}</p>
    <div class="d-flex justify-content-end align-items-start">
      <button type="button" class="ms-2" @click="deleteComment" style="">삭제</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Comment',
  components: {
  },
  props: {
    comment: {
      type: [Object,Number,String]
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
    deleteComment: function () {
      this.$emit('deleteComment', this.comment.id)
      // axios({
      //   method: 'delete',
      //   url: `http://127.0.0.1:8000/community/comments/${this.comment.id}/`,
      //   headers: this.setToken()
      // })
      //   .then((response) => {
      //     console.log(response)
      //     // 코멘트를 삭제했다 그럼 다시 데이터 요청해야하는데
      //     // 다른 곳에 있는 함수를 여기서도 써야함
      //     // 어떻게 해야할지 모르겄따;
      //   })
      //   .catch((error) => {
      //     console.log(error)
      //   })
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
    check: function () {
      console.log(this.comment.id)
    }
  }
}
</script>

<style>

</style>