<template>
  <div>
    <!-- <h1>추천 Movie Detail</h1> -->
      <div class="col">
        <div class="card">
          <img :src="'https://image.tmdb.org/t/p/w400/'+ recommend['poster_path']" alt="">
          <div class="card-body">
            <h5 class="card-title">{{ recommend['title']}}</h5>
            <p class="card-text ov1">{{ recommend['overview'] }}</p>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
export default {
 name: 'RecommendedMovie',
  props: {
    recommend: {
      type: [Object,String,Number]
    },
  },
}
</script>

<style>

.ov1 {
  margin-top: -40px;
  /* position: absolute; */
  /* visibility: hidden; */
  /* opacity: 0; */
  /* font-size: 20px; */
  /* padding:20px; */
  color: black;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 5;    /* 라인수 */
  -webkit-box-orient: vertical;
  word-wrap:break-word;
  /* line-height: 1.8rem; */
  height: 140px;
  /* min-height: 200px; */
}

</style>