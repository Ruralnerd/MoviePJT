<template>
  <div class="container">
    <h1>CommentForm</h1>
      <b-form-textarea
        id="textarea-rows"
        placeholder=""
        rows="2"
        class="col-sm-2"
        v-model="content"
      ></b-form-textarea>
  </div>
</template>

<script>
export default {
  name:'CommentForm',
}
</script>

<style>

</style>