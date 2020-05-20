<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',

}
</script>

<style>
*{
  margin: 0;
  padding: 0;
}
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
@font-face {
  font-family: "hq";
  font-display: fallback;
  src: url("./assets/SourceHanSansSC-Medium.otf") format('opentype');
}
*{
  font-family: 'hq',sans-serif!important;
}
  #app /deep/ {
    font-family: 'hq',sans-serif!important;
  }
</style>
<style>
  h1{
    font-size: 26px;
  }
  h2,h3{
    font-size: 20px;
  }
</style>