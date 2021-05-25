<template>
  <div>
    <h1>글쓰는 곳임</h1>
    <div class="container col-sm-4">
      <div class="p-1">
        <textarea class="form-control" placeholder="제목" id="floatingTitle" v-model="title" style="height:15px"></textarea>
        <!-- <label for="floatingTextarea">제목</label> -->
      </div>   
      <div class="p-1">
        <textarea class="form-control" placeholder="영화 제목" id="floatingMovieTitle" v-model="movie_title" style="height:15px"></textarea>
      </div>
      <!-- 얘는 본문임 -->
      <div class="p-1">
        <textarea class="form-control" placeholder="본문" id="floatingContent" v-model="content" style=""></textarea>
      </div>
      <b-button @click="updateDetail">수정</b-button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ArticleUpdateForm',
  data: function () {
    return {
      title: this.$route.query.title,
      movie_title: this.$route.query.movie_title,
      content: this.$route.query.content,
      id: this.$route.query.id,
    }
  },
  mounted: function () {
    if(this.query) {
      this.getDetail()
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
    getDetail: function () {
      
    },
    // 장고로 신호 쏴줘야해 ..
    updateDetail: function () {
      axios({
        method: 'put',
        url: ``,
        data:'',
        headers: this.setToken(),
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