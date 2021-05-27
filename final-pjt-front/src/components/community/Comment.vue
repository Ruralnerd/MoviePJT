<template>
  <div class='mx-5 bg-cus'>
    <div class="d-flex user-box">
      <p class="">{{comment.username}}        {{comment.created_at}}
      <button type="button" class="del-btn" @click="deleteComment" style="" v-if='comment.username === myinfo.username'>X</button></p>
    </div>
      <div class="d-flex align-items-start">
        <p class="text-start mb-0">{{ comment.content }}</p>
      </div>
  <hr>    
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'Comment',
  components: {
  },
  props: {
    comment: {
      type: [Object,Number,String]
    },
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
    padding:0px
  }

  .del-btn {
    position: relative;
    /* margin-left: 180px; */
    height: 25px;
    padding-left: 3px;
    padding-top: -2px;
    padding-right: 3px;
    /* border: 1px solid black; */
  }

  .user-box {
    height: 35px;
  }
</style>