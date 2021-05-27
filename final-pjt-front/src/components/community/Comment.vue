<template>
  <div class='ms-5 me-5 mb-2 bg-cus'>
    <div class="d-flex align-items-start user-box">
      <p>{{comment.username}}</p><p class="p-pos mt-1" style="font-size:12px">{{comment.created_at}}</p>
        <button type="button" class="del-btn" @click="deleteComment" style="">X</button>
    </div>
      <div class="d-flex align-items-start">
        <p class="text-start">{{ comment.content }}</p>
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
  .p-pos {
    position: absolute;
    margin-left: 80px;
  }

  .bg-cus {
    background-color: skyblue;
  }

  .del-btn {
    position: relative;
    margin-left: 140px;
    height: 25px;
    padding-left: 3px;
    padding-top: 0px;
    padding-right: 3px;
  }

  .user-box {
    height: 35px;
  }
</style>