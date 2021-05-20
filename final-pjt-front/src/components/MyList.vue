<template>
  <div>
    <!-- <h1>{{ mymovie.title }}</h1> -->
    <!-- variable routing이 가능할까? -->
    <h1><router-link :to="mymovie.id">{{ mymovie.title }}</router-link></h1>
    <h2>{{ mymovie.id }}</h2>
  </div>
</template>

<script>
export default {
  name: 'MyList',
  components: {

  },
  props: {
    mymovie: {
      type: Object,
    }
  }
}
</script>

<style>

</style>