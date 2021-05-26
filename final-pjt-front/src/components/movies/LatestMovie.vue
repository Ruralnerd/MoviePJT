<template>
  <div class="card img_wrap mh" style="width: 100%;">
    <img :src="'https://image.tmdb.org/t/p/w400/' + latestmovie['fields']['poster_path']" class="card-img-top hv" alt="...">
    <div class="card-body bg-primary container d-flex flex-column pb-5" style="max-height:500px">
      <p class="card-text overvie">{{latestmovie['fields']['title'] }}</p>
      <p class="card-text overview2" style="font-size:50px; color:blue;">{{latestmovie['fields']['vote_average'] }}</p>
      <p class="card-text overview2" style="font-size:50px; color:blue;">{{latestmovie['fields']['release_date'] }}</p>
    </div>
  </div>
</template>

<script>

export default {
  name: "LatestMovie",
  components: {
  },
  props: {
    latestmovie: {
      type: Object,
    },
  },
}
</script>

<style>

  .img_wrap:hover .overview2 {
    visibility: visible;
    opacity: 1;
  }
  
  .hv:hover {
    opacity: 0.5;
  }

  .overview2 {
    position: relative;
    margin-top: -200px;
    visibility: hidden;
    opacity: 0;
    font-size: 15px;
  }

  .mh {
    min-height: 55vh;
  }
</style>