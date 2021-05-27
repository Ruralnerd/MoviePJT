<template>
  <div>
    <div class="container col-sm-5 mt-5 px-5 bg-gray pb-5">
      <h1 class="text-start px-3 pt-3">글쓰기</h1>
      <div class="input-group mb-3 p-3">
        <span class="input-group-text">제목</span>
        <input type="text" class="form-control" placeholder="제목을 입력하세요." v-model="title" maxlength="31" aria-label="title">
        <br>
      </div>   
      <div class="input-group mb-3 px-3">
        <span class="input-group-text">영화</span>
        <input type="text" class="form-control" placeholder="영화 제목을 입력하세요." v-model="movie_title" maxlength="31" aria-label="movie_title">
        <br>
      </div>   
      <div class="p-3">
        <textarea class="form-control" placeholder="" id="floatingContent" v-model="content" maxlength="279" style="height:150px"></textarea>
      </div>
      <br>
      <div class="d-flex flex-row-reverse px-3">
        <button type="button" @click="createArticle" class="">작성</button>
      </div>
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
        movie_title: this.movie_title,
        id: this.id
      }
      // console.log(Article)
      // 값이 있다면
      if (Article.title) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/community/review/',
          data: Article,
          headers: this.setToken()
        })
          .then((response) => {
            console.log(response)
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