<template>
  <div class="container col-sm-6 mt-3" style="width:40%">
    <div class="bg1 p-5">
      <b-form class="">
      <h1 class="p-3">회원가입</h1>
      <!-- 아이디 -->
      <b-form-group id="input-group-1" label="아이디" label-for="username" class="text-start">
        <b-form-input id="username" v-model="credentials.username" type="text" maxlength="8" placeholder="아이디는 8자까지 입력 가능합니다." class=""></b-form-input>
      </b-form-group>
      <br>
      <!-- 비밀번호 -->
      <b-form-group id="input-group-2" label="비밀번호" label-for="password" class="text-start">
        <b-form-input id="password" v-model="credentials.password" type="password" maxlength="12" placeholder="비밀번호는 12자까지 입력 가능합니다."></b-form-input>
      </b-form-group>
      <br>
      <!-- 비밀번호 확인 -->
      <b-form-group id="input-group-3" label="비밀번호 확인" label-for="passwordconfirmation" class="text-start">
        <b-form-input id="passwordconfirmation" v-model="credentials.passwordConfirmation" maxlength="12"  type="password" placeholder="비밀번호를 재입력해 주세요."></b-form-input>
      </b-form-group>
      <br>
      <!-- 회원가입 버튼 -->
      <button type="button" class="" @click="signup(credentials)">가입</button>
      </b-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    signup: function () {
      console.log(this.credentials)
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials
      })
        .then(response => {
          console.log(response)
          this.$router.push({ name: 'Signin' })
        })
        .catch(error => {
          console.log(error)
        })
    },
  }
}
</script>

<style>

</style>