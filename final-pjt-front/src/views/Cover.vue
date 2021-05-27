<template>
  <div class="">
    <div class="" style="padding:0px;">
        <!-- <div style=""><img src="https://i.ibb.co/zrNx6F7/cover.jpg" class="wp"></div> -->
        <div style=""><img src="https://i.imgur.com/1Qsqd6m.jpg" class="wp"></div>
    </div>
    <div class="box14 d-flex w-50">
      <div class="box15 container d-flex flex-column w-50">
        <p class="cover-p">아직 회원이 아니라면</p>
        <router-link :to="{ name: 'Signup' }" class="text-decoration-none"><button type="button" class="qq">회원가입</button></router-link>
      </div>
      <div class="box15 container d-flex flex-column w-50">
        <p class="cover-p">이미 회원이신가요?</p>
        <router-link :to="{ name: 'Signin' }" class="text-decoration-none"><button type="button" class="qq">로그-인</button></router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name:'Cover'
}
</script>

<style>
.wp {
  position: relative;
  padding-top: 0;
  max-width: 100%;
  max-height: 100%;
  /* height: 100vh; */
  /* margin-left: 1px; */
  /* border: 10px solid red;  */
}

.qq {
  padding: 10px;
}

/* .l {
  margin-left: -20vmin;
  padding: 15px;
}
.r {
  padding: 15px;
  margin-left: 11vw;
  margin-right: 100px;
} */

.cover-p {
  font-size: 20px;
}

/* .r-p {
  margin-left: 35vw;
  font-size: 20px;
}

.l-p {
  margin-left: 58vw;
  font-size: 20px;
} */

.box15 {
  /* border: 3px solid blue; */

}

.box14 {
  /* border: 3px solid red; */
  position: absolute;
  margin-top: -300px;
  margin-left: 400px;
}
</style>