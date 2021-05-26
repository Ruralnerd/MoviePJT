<template>
  <div>
    <div class="container col-sm-6">
      <div class="p-1 mt-5">
        <textarea class="form-control" placeholder="제목" id="floatingTitle" v-model="title" style="height:15px"></textarea>
        <!-- <label for="floatingTextarea">제목</label> -->
        <br>
      </div>   
      <div class="p-1">
        <textarea class="form-control" placeholder="영화 제목" id="floatingMovieTitle" v-model="movie_title" style="height:15px"></textarea>
        <br>
      </div>
      <!-- 얘는 본문임 -->
      <div class="p-1">
        <textarea class="form-control" placeholder="본문" id="floatingContent" v-model="content" style="height:150px"></textarea>
      </div>
      <br>
      <div class="d-flex flex-row-reverse">
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
      console.log(Article)
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