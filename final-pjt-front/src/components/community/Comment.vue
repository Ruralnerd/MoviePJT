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
  methods: {
    check: function () {
      console.log(this.comment)
    }
  }
}
</script>

<style>

</style>