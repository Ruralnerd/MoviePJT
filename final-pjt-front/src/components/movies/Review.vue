<template>
  <div>
    <!-- <h1>Review</h1> -->
    <!-- <p>{{ review.user }}</p> -->
    <p>{{ review.star }}점  {{ review.opinion }}</p>
  </div>
</template>

<script>

export default {
  name: 'Review',
  props: {
    review: {
      type:Object
    }
  }
}
</script>

<style>

</style>