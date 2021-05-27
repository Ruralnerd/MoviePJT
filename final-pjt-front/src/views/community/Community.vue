<template>
  <div class="container col-sm-8 mt-5" style="">
    <div class="d-flex box3">
      <h1>자유 게시판</h1>
      <router-link :to="{ name: 'ArticleForm' }" class="text-decoration-none d-flex flex-column justify-content-center"><button type="button">글쓰기</button></router-link>
    </div>
    <table class="table table-dark table-hover">
      <thead>
        <tr>
          <th scope="col">글번호</th>
          <th scope="col">제목</th>
          <th scope="col">작성자</th>
          <th scope="col">등록일</th>
        </tr>
      </thead>
      <tbody>
          <Article
            v-for="(article, idx) in articles"
            :key="idx"
            :article="article"
          />
      </tbody>
    </table>    
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
        url: 'http://127.0.0.1:8000/community/review/',
        headers: this.setToken()
      })
        .then((response) => {
          this.articles = response.data.reverse()
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
  h1 {
    color:yellow
  }

</style>