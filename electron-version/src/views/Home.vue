<template>
  <div class="home">
    <h1>Mgek ImgBed图床</h1>
    <p style="color: #a0a0a0;font-size: 12px">just for test, version 3.1</p>
    <div class="upart">
      <p>如果你没有使用过本软件请查看教程</p>
      <el-button type="success" @click="help">教程</el-button>
      <p>如果首次使用请前往配置</p>
      <el-button type="primary" @click="config">配置</el-button>
      <p>查看本软件的详细信息</p>
      <el-button type="info" @click="about">关于本软件</el-button>
      <i class="el-icon-picture" style="position: absolute;bottom: 10px;right: 40px;cursor: pointer;font-size: 20px" @click="image_list"></i>
      <i class="el-icon-upload" style="position: absolute;bottom: 10px;right: 10px;cursor: pointer;font-size: 20px" @click="home"></i>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import  {shell} from 'electron';
export default {
  name: 'Home',
  data(){
    return{

    }
  },
  methods:{
    help(){
      shell.openExternal('https://github.com/Landers1037/mgek_imgbed/blob/master/help.md');
    },
    config(){
      this.$router.push('/config');
    },
    home(){
      this.$router.push('/home')
    },
    about(){
      this.$router.push('/about')
    },
    image_list(){
      this.$router.push('/image_list')
    }
  }
}
</script>

<style scoped>
  .home {padding: 20px;font-family: 'hq',sans-serif}
  .home .upart{
    padding: 26px 10px 26px 10px;
    background-color: #e0e0e0;
    margin-top: 40px;
    border-radius: 6px;
    position: relative;
  }
  .upart p{
    padding: 8px 0;
    font-size: 13px;
  }
</style>
