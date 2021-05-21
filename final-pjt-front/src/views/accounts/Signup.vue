<template>
  <div class="box bg-success w-50 container col-sm-2">
    <b-form class="">
      <h1>Sign up page</h1>
      <!-- 아이디 -->
      <b-form-group id="input-group-1" label="User name" label-for="username">
        <b-form-input id="username" v-model="credentials.username" type="text" placeholder="ID를 입력해 주세요." class=""></b-form-input>
      </b-form-group>
      <br>
      <!-- 비밀번호 -->
      <b-form-group id="input-group-2" label="Password" label-for="password">
        <b-form-input id="password" v-model="credentials.password" type="password" placeholder="●●●●●●●●"></b-form-input>
      </b-form-group>
      <br>
      <!-- 비밀번호 확인 -->
      <b-form-group id="input-group-3" label="PasswordCheck" label-for="passwordcheck">
        <b-form-input id="passwordcheck" v-model="credentials.passwordCheck" type="password" placeholder="●●●●●●●●"></b-form-input>
      </b-form-group>
      <br>
      <!-- 회원가입 버튼 -->
      <b-button @click="signup(credentials)">회원가입</b-button>
      <hr>
      </b-form>
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordCheck: null,
      }
    }
  },
  methods: {
    signup: function () {
      console.log(this.credentials)
      // axios({
      //   method: 'post',
      //   // url 이따 쓸 것
      //   url: '#',
      //   data:this.credentials
      // })
      //   .then(response => {
      //     console.log(response)
      //     console.log(this.credentials)
      //   })
      //   .catch(error => {
      //     console.log(error)
      //   })
    }
  }
}
</script>

<style>

</style>