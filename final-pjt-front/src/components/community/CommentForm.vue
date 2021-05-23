<template>
  <div>
    <h1>CommentForm</h1>
      <b-form-textarea
        id="textarea-rows"
        placeholder=""
        rows="6"
        class=""
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