<template>
  <div class="card img_wrap mh" style="width: 100%;">
    <img :src="'https://image.tmdb.org/t/p/w400/' + popularmovie['fields']['poster_path']" class="card-img-top hv" alt="...">
    <div class="card-body bg-primary container d-flex flex-column pb-5" style="max-height:500px">
      <p class="card-text overvie">{{popularmovie['fields']['title'] }}</p>
      <p class="card-text overview2" style="font-size:50px; color:blue;">{{popularmovie['fields']['vote_average'] }}</p>
      <p class="card-text overview2" style="font-size:50px; color:blue;">{{popularmovie['fields']['release_date'] }}</p>
    </div>
  </div>
</template>

<script>

export default {
  name: "popularMovie",
  components: {
  },
  props: {
    popularmovie: {
      type: Object,
    },
  },
}
</script>

<style>

 .card-text {
   font-size: 1.2rem;
 }

</style>