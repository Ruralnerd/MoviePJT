<template>
  <div>
    <div class="container col-sm-6 mt-4 px-5">
      <h1 class="text-start px-3">글쓰기</h1>
      <div class="input-group mb-3 p-3">
        <span class="input-group-text">제목</span>
        <input type="text" class="form-control" :placeholder=updatearticle.title v-model="updatetitle" maxlength="31" aria-label="title">
        <br>
      </div>   
      <div class="input-group mb-3 px-3">
        <span class="input-group-text">영화</span>
        <input type="text" class="form-control" :placeholder=updatearticle.movie_title v-model="updatemovie_title" maxlength="31" aria-label="movie_title">
        <br>
      </div>   
      <div class="p-3">
        <textarea class="form-control" :placeholder=updatearticle.content id="floatingContent" v-model="updatecontent" maxlength="279" style="height:150px"></textarea>
      </div>
      <br>
      <div class="d-flex flex-row-reverse px-3">
        <button type="button" @click="updateDetail" class="">수정</button>
      </div>
    </div>    
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'ArticleUpdateForm',
  data: function () {
    return {
      updatetitle: null,
      updatemovie_title: null,
      updatecontent: null,
    }
  },
  computed: {
    ...mapState([
      'updatearticle',
    ])
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
      const Article = {
        title: this.updatetitle,
        content: this.updatecontent,
        movie_title: this.updatemovie_title,
        user: this.updatearticle.user
      }
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/community/review/${this.updatearticle.id}/`,
        data:Article,
        headers: this.setToken(),
      })
        .then((response) => {
          console.log(response)
          this.$router.push({ name: 'Community' })
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