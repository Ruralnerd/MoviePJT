<template>
  <div>
    <h1>커뮤니티 페이지</h1>
    <!-- <b-button @click=>글쓰기</b-button> -->
    <router-link :to="{ name: 'ArticleForm' }" class="text-decoration-none p-2"><b-button>글쓰기</b-button></router-link>
    <ul>
      <!-- 가져온 데이터(articles)를 반복문을 통해 보여주자 -->
      <!-- django model과 합을 맞춰야 할 것 같다. -->
      <Article
        v-for="(article, idx) in articles"
        :key="idx"
        :article="article"
      />
        <!-- <p>{{ article.title }}</p> 제목 -->
        <!-- <p>{{ article.created_at }}</p> 작성시간 -->
        <!-- <p>{{ article.user }}</p> 작성자 -->
        <!-- 각 글에 답글이 몇개씩 달렸는지도 해볼까? -->
    </ul>
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
        url: 'http://127.0.0.1:8000/community/',
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
    this.getArticles()
  }
}
</script>

<style>

</style>