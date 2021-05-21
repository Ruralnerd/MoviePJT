<template>
<!-- 이따 와서 중앙정렬 할 것 -->
  <div class="container box bg-success w-50 col-sm-2 form-floating">
    <b-form class="">
      <h1>Sign in page</h1>
      <!-- 아이디 -->
      <b-form-group id="input-group-1" label="User name" label-for="username">
        <b-form-input id="username" v-model="credentials.username" type="text" placeholder="ID를 입력해 주세요." class="form-control"></b-form-input>
      </b-form-group>
      <br>
      <!-- 비밀번호 -->
      <b-form-group id="input-group-2" label="Password" label-for="password">
        <b-form-input id="password" v-model="credentials.password" type="password" placeholder="●●●●●●●●"></b-form-input>
      </b-form-group>
      <br>
      <!-- 로그인 버튼 -->
      <b-button @click="signin">로그인</b-button>
      <hr>
      </b-form>
  </div>
</template>

<script>
// import axios from 'axios'


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
      console.log(this.credentials)
      // axios({
      //   method: 'post',
      //   // url 안달아줬다 jwt 방식 쓸것인가?
      //   url: '#',
      //   data: this.credentials
      // })
      //   .then(response => {
      //     console.log(response)
      //   })
      //   .catch(error => {
      //     console.log(error)
      //   })
    }
  }
}
</script>

<style>
  .box {
    border: 1px solid black;
  }
</style>