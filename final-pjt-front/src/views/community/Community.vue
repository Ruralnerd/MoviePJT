<template>
  <div>
    <h1>커뮤니티 페이지</h1>
    <!-- <b-button @click=>글쓰기</b-button> -->
    <router-link :to="{ name: 'ArticleForm' }" class="text-decoration-none p-2"><b-button>글쓰기</b-button></router-link>
    <ul>
      <!-- 가져온 데이터(articles)를 반복문을 통해 보여주자 -->
      <!-- django model과 합을 맞춰야 할 것 같다. -->
      <li v-for="(article, idx) in articles" :key="idx" >
        <p>{{ article.title }}</p> <!-- 제목 -->
        <p>{{ article.created_at }}</p> <!-- 작성시간 -->
        <p>{{ article.user }}</p> <!-- 작성자 -->
        <!-- 각 글에 답글이 몇개씩 달렸는지도 해볼까? -->
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Community',
  data: function () {
    return {
      articles: null,
    }
  },
  methods: {
    getArticles: function () {

      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/community/',
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