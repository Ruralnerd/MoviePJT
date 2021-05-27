<template>
  <div class="container col-sm-6 mt-3" style="width:40%">
    <div class="bg1 p-5">
      <b-form class="">
        <h1 class="p-3">로그-인</h1>
        <!-- 아이디 -->
        <b-form-group id="input-group-1" label="아이디" label-for="username" class="text-start">
          <b-form-input id="username" v-model="credentials.username" type="text" maxlength="8" placeholder="아이디를 입력해 주세요." class="form-control"></b-form-input>
        </b-form-group>
        <br>
        <!-- 비밀번호 -->
        <b-form-group id="input-group-2" label="비밀번호" label-for="password" class="text-start">
          <b-form-input id="password" v-model="credentials.password" maxlength="12" type="password" placeholder="●●●●●●●●"></b-form-input>
        </b-form-group>
        <br>
        <!-- 로그인 버튼 -->
        <button type="button" class="mt-3" @click="signin">로그-인</button>
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
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials
      })
        .then(response => {
          this.$emit('signin')
          console.log(response)
          localStorage.setItem('jwt', response.data.token)
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

.bg1 {
  background-color:	#0000CD ;
  color:white;
}
</style>