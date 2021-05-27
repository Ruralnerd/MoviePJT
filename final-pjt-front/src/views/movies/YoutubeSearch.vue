<template>
  <div class="container col-sm-8 mt-5 bg-light pt-3" style="border: 3px solid black; border-radius: 5px;">
      <textarea
        class="form-control mb-5"
        placeholder="검색어를 입력해 주세요."
        id="floatingTitle" v-model="inputText"
        style="height:10px;"
        @keyup.enter="check"
      ></textarea>
      <!-- <h3>{{ video }}</h3> -->
      <iframe width="100%" height="600px" :src="'https://www.youtube.com/embed/'+ video" frameborder="0"></iframe>
  </div>
</template>

<script>
import axios from 'axios'
import { Glide, GlideSlide } from 'vue-glide-js'
import { mapState } from 'vuex'

export default {
  name: "YoutubeSearch",
  components: {
    [Glide.name]: Glide,
    [GlideSlide.name]: GlideSlide   
  },
  computed: {
    ...mapState([
      'movies',
    ])
  },
  data: function () {
    return {
      inputText: '',
      video: null,
    }
  },
  methods: {
    check: function () {
      const params = {
          // 검색어
          q: this.inputText,
          key: 'AIzaSyBUvmbY05VK189xkC20cl0hWR5b6027Sns',
          part: 'snippet',
          type: 'video'
        }
        
      axios({
        method: 'get',
        url: 'https://www.googleapis.com/youtube/v3/search',
        params
      })
        .then(res => {
          this.inputText = ''
          this.video = res.data.items[0].id['videoId']
        })
        .catch(err => console.log(err))
    },
  }
}
</script>

<style>


</style>