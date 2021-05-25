<template>
  <div>
    <h1>Recommended Movie List</h1>
    <p>{{ removies }}</p>
  </div>
</template>

<script>

export default {
  name: 'Recommended',
  computed: {
    recommendMovie: function () {
      return this.$store.getters.recommendMovie
    },
  }
}
</script>

<style>

</style>