<template>
  <div class="d-flex justify-content-between container m-2 cnt">
    <div class="ms-5">
      <p><router-link :to="`/articledetail/${article.id}`" class="text-decoration-none p-2">{{ article.title }}</router-link>[{{ article.comment_count }}]</p>
    </div>
    <div class="me-5">
      <p class="">{{ article.created_at }}</p>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Article',
  components: {
  },
  props: {
    article: {
      type: Object,
    },
  },
}
</script>

<style>
  .cnt {
    padding-left: 100px;
    padding-right: 100px;
  }

  .bgc {
    background-color: aliceblue;
  }
</style>