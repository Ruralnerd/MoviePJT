<template>
  <div>
    <h1>Article(게시글 디테일 보여줄 곳)</h1>
    <Comment
      v-for="(comment, idx) in comments"
      :key="idx"
      :comment="comment"
    />
    <!-- <CommentForm/> -->
  </div>
</template>

<script>
// import axios from 'axios'
import Comment from '@/components/community/Comment'
// import CommentForm from '@/components/community/CommentForm'


export default {
  // article에서 comment를 가져와서 props 시켜주자
  name: 'Article',
  components: {
    Comment,
    // CommentForm
  },
  props: {
    article: {
      type: Object,
    }
  },
  data () {
    return {
      comments:[],
    }
  },
  methods: {
    // getComments () {
    //   axios({
    //     method: 'get',
    //     url: '#',
    //     // headers?
    //   })
    //     .then((response) => {
    //       this.comments = response.data
    //     })
    //     .catch((error) => {
    //       console.log(error)
    //     })
    // }
  }
}
</script>

<style>

</style>