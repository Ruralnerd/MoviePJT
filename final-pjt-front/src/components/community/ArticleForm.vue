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
      <b-button @click="createArticle">작성</b-button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ArticleForm',
  data: function () {
    return {
      title: '',
      movie_title: '',
      content: '',
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
    // 장고로 신호 쏴줘야해 ..
    createArticle: function() {
      const Article = {
        title: this.title,
        content: this.content,
        movie_title: this.movie_title
      }
      console.log(Article)
      // 값이 있다면
      if (Article.title) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/api/community/review/',
          data: Article,
          headers: this.setToken()
        })
          .then((response) => {
            console.log(response)
            // 글 작성이 완료되면 어디로 보내줄까?
            this.$router.push({ name: 'Community' })
          })
          .catch((error) => {
            console.log(error)
          })
      }
    },
  }
}
</script>

<style>

</style>