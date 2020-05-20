<template>
  <div class="about">
    <h1>关于本软件</h1>
    <i class="el-icon-arrow-left" style="position: absolute;left: 15px;top: 15px;font-weight:bold" @click="home"></i>
    <p style="color: #a0a0a0;font-size: 14px">
      一个rest的图床服务，支持注册用户通过token访问服务。<br>支持sqlite和MongoDB数据库模式。可以通过配置文件随意切换<br>
      用户可以通过邮箱获取token，通过邮件方式找回token或者注销账户
    </p>
    <div style="margin-top: 30px;text-align: left;padding: 0 70px">
      <p><span>作者：</span><span style="color: forestgreen;margin-right: 6px">{{copyright}}</span><span>Github: <a style="color: slateblue;cursor: pointer" @click="go(github1)">{{github1}}</a></span></p>
      <p><span>贡献者：</span><span style="color: forestgreen;margin-right: 6px">{{contributor1}}</span><span>Github: <a style="color: slateblue;cursor: pointer" @click="go(github2)">{{github2}}</a></span></p>
      <p><span>贡献者：</span><span style="color: forestgreen;margin-right: 6px">{{contributor2}}</span><span>Github: <a style="color: slateblue;cursor: pointer" @click="go(github3)">{{github3}}</a></span></p>
    </div>
    <div style="margin-top: 20px;text-align: left;padding: 0 70px">
      <p>感谢各位贡献者的贡献，才有了这个项目</p>
      <p>项目地址： <a style="color: slateblue;cursor: pointer" @click="go(project)">{{project}}</a></p>
    </div>
  </div>
</template>

<script>
  import {shell} from 'electron';
  export default {
    name: 'About',
    data(){
      return{
        copyright: 'Landers1037',
        github1: 'github.com/landers1037',
        contributor1: 'xkwang',
        github2: 'github.com/xkwang',
        project: 'github.com/landers1037/mgek_imgbed'
      }
    },
    methods:{
      go(link){
        let reallink = 'https://' + link;
        shell.openExternal(reallink);
      },
      home(){
        this.$router.push('/')
      }
    }
  }
</script>
<style scoped>
  .about{
    padding: 20px ;
    position: relative;
  }
</style>
