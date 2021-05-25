<template>
  <div>
    <h1>추천 Movie Detail</h1>
  </div>
</template>

<script>
export default {
 name: 'RecommendedMovie',
  computed: {
    recommendMovie: function () {
      return this.$store.getters.recommendMovie
    },
  }
}
</script>

<style>

</style>