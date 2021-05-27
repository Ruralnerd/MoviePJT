<template>
  <div class="mt-3">
    <img :src="'https://image.tmdb.org/t/p/w400/' + result['poster_path']" class="card-img-top" @error="myFunc" alt="엑박이요" :id="'imgTag'+result.id">
    <div class="card-body bg-light">
      <!-- <h5 class="card-title" style="color:black">Card title</h5> -->
      <p class="card-text" style="color:black">{{result['title']}}</p>
    </div>    
  </div>
</template>

<script>
export default {
  name:'Search',
  props: {
    result: {
      type:[Object,String,Number]
    },
    cat: {
      type:[Object,String,Number]
    }
  },
  methods: {
    myFunc:function() {
      document.getElementById(`imgTag${this.result.id}`).setAttribute('src', `${this.cat[0].url}`)
    }
  }
}
</script>

<style>

</style>