<template>
  <div>
    <h1>글쓰는 곳임</h1>
    <div class="container col-sm-4">
      <!-- 제목 -->
      제목 :
      <b-form-textarea
        id="textarea-state"
        v-model="title"
        :state="title.length >= 1"
        placeholder="제목을 입력해주세요."
        max-rows="1"
        rows="1"
      ></b-form-textarea>
      <!-- 얘는 본문임 -->
      <hr>
      <b-form-textarea
        id="textarea-rows"
        placeholder=""
        rows="6"
        class=""
        v-model="content"
      ></b-form-textarea>
      <hr>
      <b-button @click="createArticle">작성</b-button>
    </div>
  </div>
</template>

<script>

// import axios from 'axios'

export default {
  name: 'ArticleForm',
  data: function () {
    return {
      title: '',
      content: '',
    }
  },
  methods: {
    // 장고로 신호 쏴줘야해 ..
    createArticle: function() {
      const Article = {
        title: this.title,
        content: this.content
      }
      console.log(Article)
      this.$router.push({ name: 'Community' })
      // axios({
      //   method: 'post',
      //   url: '#',
      //   data: Article
      //   // headers?
      // })
      //   .then((response) => {
      //     console.log(response)
      //     // 글 작성이 완료되면 어디로 보내줄까?
      //     this.$router.push({ name: 'Community' })
      //   })
      //   .catch((error) => {
      //     console.log(error)
      //   })
    }
  }
}
</script>

<style>

</style>