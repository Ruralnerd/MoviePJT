<template>
  <div class="container box bg-light w-50 col-sm-2 mt-3">
    <div class="bg1 p-5">
      <b-form class="">
      <h1 class="p-3">Sign up page</h1>
      <!-- 아이디 -->
      <b-form-group id="input-group-1" label="아이디" label-for="username" class="text-start">
        <b-form-input id="username" v-model="credentials.username" type="text" placeholder="ID를 입력해 주세요." class=""></b-form-input>
      </b-form-group>
      <br>
      <!-- 비밀번호 -->
      <b-form-group id="input-group-2" label="비밀번호" label-for="password" class="text-start">
        <b-form-input id="password" v-model="credentials.password" type="password" placeholder="●●●●●●●●"></b-form-input>
      </b-form-group>
      <br>
      <!-- 비밀번호 확인 -->
      <b-form-group id="input-group-3" label="비밀번호 확인" label-for="passwordconfirmation" class="text-start">
        <b-form-input id="passwordconfirmation" v-model="credentials.passwordConfirmation" type="password" placeholder="●●●●●●●●"></b-form-input>
      </b-form-group>
      <br>
      <!-- 회원가입 버튼 -->
      <button type="button" class="btn bg-light" @click="signup(credentials)">회원가입</button>
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
        // url 이따 쓸 것
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials
      })
        .then(response => {
          console.log(response)
          // console.log(this.credentials)
          this.$router.push({ name: 'Signin' })
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

</style>