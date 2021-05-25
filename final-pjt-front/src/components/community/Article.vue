<template>
  <tr>
    <th scope="row">{{article.id}}</th>
    <td><router-link :to="`/articledetail/${article.id}`" class="text-decoration-none p-2">{{ article.title }}[{{ article.comment_count }}]</router-link></td>
    <td>작성자</td>
    <td>{{ article.created_at }}</td>
  </tr>
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