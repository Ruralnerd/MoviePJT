<template>
  <div>
    <img :src="'https://image.tmdb.org/t/p/w400/' + result['poster_path']" class="card-img-top" onError="this.src='https://lh3.googleusercontent.com/proxy/Fu5FrnTc3PX2GTnTd1VLkOl8CuHUNpYfB73rAc6qHQO-2SBgHOmw_1HgLHUXwfrPEQvwUR-YOm7_Yo-lAp96w9eTVAKX-cvsUZHLW3ZRR58o9pk1OA'" alt="엑박이요">
    <div class="card-body">
      <h5 class="card-title">Card title</h5>
      <p class="card-text">{{result['title']}}</p>
      <a href="#" class="btn btn-primary">Go somewhere</a>
    </div>    
  </div>
</template>

<script>
export default {
  name:'Search',
  props: {
    result: {
      type:[Object,String,Number]
    }
  }
}
</script>

<style>

</style>