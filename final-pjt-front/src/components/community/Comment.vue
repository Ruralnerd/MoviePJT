<template>
  <div>
    <h1>Comment</h1>
    <CommentForm/>
  </div>
</template>

<script>
import CommentForm from '@/components/community/CommentForm.vue'

export default {
  name: 'Comment',
  components: {
    CommentForm
  },
  props: {
    comment: {
      type: Object,
    },
  },
}
</script>

<style>

</style>