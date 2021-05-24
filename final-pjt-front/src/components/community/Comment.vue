<template>
  <div>
    <p>{{ comment.content }}</p>
  </div>
</template>

<script>


export default {
  name: 'Comment',
  components: {
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