<template>
  <div>
    <h1>커뮤니티 페이지</h1>
    <ul>
      <Article
        v-for="(article, idx) in articles"
        :key="idx"
        :article="article"
      />
    </ul>
    <router-link :to="{ name: 'ArticleForm' }" class="text-decoration-none p-2"><b-button>글쓰기</b-button></router-link>
  </div>
</template>

<script>
import axios from 'axios'
import Article from '@/components/community/Article.vue'

export default {
  name: 'Community',
  components: {
    Article
  },
  data: function () {
    return {
      articles: null,
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
    getArticles: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/community/review/',
        headers: this.setToken()
      })
        .then((response) => {
          this.articles = response.data
        })
        .catch((error) => {
          console.log(error)
        })

    }
  },
  // 페이지가 열리자마자 글을 가져오게하자
  created: function () {
    // if (localStorage.getItem('jwt')) {
    this.getArticles()
    // } else {
      // this.$router.push({name: 'Login'})
    // }
  }
}
</script>

<style>

</style>