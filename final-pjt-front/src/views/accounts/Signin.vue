<template>
<!-- 이따 와서 중앙정렬 할 것 -->
  <div class="container box bg-light w-50 col-sm-2 mt-3">
    <div class="bg1 p-5">
      <b-form class="">
        <h1 class="p-3">Sign in page</h1>
        <!-- 아이디 -->
        <b-form-group id="input-group-1" label="아이디" label-for="username" class="text-start">
          <b-form-input id="username" v-model="credentials.username" type="text" placeholder="ID를 입력해 주세요." class="form-control"></b-form-input>
        </b-form-group>
        <br>
        <!-- 비밀번호 -->
        <b-form-group id="input-group-2" label="비밀번호" label-for="password" class="text-start">
          <b-form-input id="password" v-model="credentials.password" type="password" placeholder="●●●●●●●●"></b-form-input>
        </b-form-group>
        <br>
        <!-- 로그인 버튼 -->
        <button type="button" class="btn bg-light" @click="signin">로그인</button>
      </b-form> 
    </div>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name : 'Signin',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    signin: function () {
      // console.log(this.credentials)
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials
      })
        .then(response => {
          console.log(response)
          localStorage.setItem('jwt', response.data.token)
          // this.$emit('signin')
          this.$router.push({ name: 'Main' })
        })
        .catch(error => {
            console.log(error)
        })

    }
  }
}
</script>

<style>
.box {
  border: 2px solid black;
  border-radius: 5px;
}

.bg1 {
  background-color:blue;
  /* color: aqua; */
  color:white;
}
</style>