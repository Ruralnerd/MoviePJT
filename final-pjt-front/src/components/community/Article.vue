<template>
  <div>
    <p><router-link :to="`/articledetail/${article.id}`" class="text-decoration-none p-2">{{ article.title }}</router-link>[{{ article.comment_count }}]</p>

    <!-- <CommentForm/> -->
  </div>
</template>

<script>
// import axios from 'axios'

// import CommentForm from '@/components/community/CommentForm'

export default {
  // article에서 comment를 가져와서 props 시켜주자
  name: 'Article',
  components: {
    // Comment,
    // CommentForm
  },
  props: {
    article: {
      type: Object,
    },
  },
  data () {
    return {
      comments:[],
    }
  },
  // methods: {
    // }
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    // getComments () {
    //   axios({
    //     method: 'get',
    //     url: `http://127.0.0.1:8000/api/community/review/${this.article.id}/comments/`,
    //     // headers?
    //   })
    //     .then((response) => {
    //       this.comments = response.data
    //       console.olg(this.comments)
    //     })
    //     .catch((error) => {
    //       console.log(error)
    //     })
    // },
    // created: function () {
    //   this.getComments()
    // }
  }
}
</script>

<style>

</style>