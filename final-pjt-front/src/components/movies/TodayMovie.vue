<template>
  <div class="card img_wrap mh" style="width: 100%;">
    <img :src="'https://image.tmdb.org/t/p/w400/' + todaymovie['fields']['poster_path']" class="card-img-top hv" alt="...">
    <div class="card-body bg-primary container d-flex flex-column pb-5" style="max-height:500px">
      <p class="card-text overvie">{{todaymovie['fields']['title'] }}</p>
      <p class="card-text overview2" style="font-size:50px; color:blue;">{{todaymovie['fields']['vote_average'] }}</p>
      <p class="card-text overview2" style="font-size:50px; color:blue;">{{todaymovie['fields']['release_date'] }}</p>
    </div>
  </div>
</template>

<script>

export default {
  name: "todayMovie",
  components: {
  },
  props: {
    todaymovie: {
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