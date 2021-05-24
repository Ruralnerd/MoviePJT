<template>
  <div>
    <h1>글쓰는 곳임</h1>
    <div class="container col-sm-4">
      <!-- 제목 -->
      제목 :
      <b-form-textarea
        id="textarea-rows"
        v-model="title"
        placeholder="제목을 입력해주세요."
        rows="1"
      ></b-form-textarea>
      <!-- 얘는 본문임 -->
      <hr>
      <b-form-textarea
        id="textarea-rows"
        v-model="content"
        placeholder=""
        rows="2"
        class=""
      ></b-form-textarea>
      <hr>
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
      title: null,
      content: null,
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
        content: this.content
      }

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
        // console.log(Article)
        // this.$router.push({ name: 'Community' })
    }
  }
}
</script>

<style>

</style>