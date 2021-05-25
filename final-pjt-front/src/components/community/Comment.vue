<template>
  <div class="d-flex">
    <p>{{ comment.content }}</p>
    <button type="button" class="btn btn-danger ms-3" @click="deleteComment">삭제</button>
    <button @click="check">체크</button>
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
      type: Object,
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
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/api/community/comments/${this.comment.id}/`,
        headers: this.setToken()
      })
        .then((response) => {
          console.log(response)
          // 코멘트를 삭제했다 그럼 다시 데이터 요청해야하는데
          // 다른 곳에 있는 함수를 여기서도 써야함
          // this.getComments()
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