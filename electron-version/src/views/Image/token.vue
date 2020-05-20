<template>
    <div class="token">
        <h3>获取你的token</h3>
        <i class="el-icon-arrow-left" style="position: absolute;left: 15px;top: 15px;font-weight:bold" @click="home"></i>
        <p style="color: red;font-size: 12px">再次生成token时原有的邮箱所对应的token会被清空</p>
        <p style="color: #42b983;font-size: 12px">如果需要使用原有的邮箱账户请找回token</p>
        <div class="token_part">
            <el-input v-model="mail" placeholder="你的邮箱地址" style="width: 300px;margin-bottom: 10px"></el-input>
            <el-button @click="gen_token">生成token</el-button>
            <el-input style="width: 90%" v-model="token">
                <template>
                    <span slot="prepend">你的token</span>
                </template>
            </el-input>
            <el-button type="danger" style="margin-top: 30px" @click="delete_token">清除token</el-button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "token",
        data(){
            return{
                mail: '',
                token: ''
            }
        },
        mounted(){
          //先从本地查找token信息
          this.mail = localStorage.getItem('mail')?localStorage.getItem('mail'): '';
          this.token = localStorage.getItem('token')?localStorage.getItem('token'):'';
        },
        methods:{
            home(){
                this.$router.push('/')
            },
            gen_token(){
                let _this =this;
                let mail = this.mail;
                if(mail.indexOf('@') === -1 ||  mail === ''){
                    _this.$message.error('请填写正确的邮箱格式')
                }else{
                    _this.$axios.post('/api/get_token',{"mail": mail}).then(res=>{
                        if(res.data.token === 'already exist'){
                            _this.$message('账户已存在')
                        }else if(res.data.token === ''){
                            _this.$message('token生成失败')
                        }else{
                            _this.token = res.data.token;
                            _this.$store.commit('updateToken',{"mail":_this.mail,"token":res.data.token});
                            _this.$message('token生成成功')
                        }
                    })
                }
            },
            delete_token(){
                //后台同时删除
                this.$axios.get('/api/remove_token?mail=' + this.mail + '&token=' + this.token).then(res=>{
                    if(res.data.type === 'error'){
                        this.$message.error('删除失败');
                    }else{
                        this.$store.commit('updateToken',{"mail": '',"token":''});
                        localStorage.setItem('token','');
                        localStorage.setItem('mail','');
                        this.mail = '';
                        this.token = '';
                        this.$message({type: 'success',message: 'token删除成功'});
                    }
                }).catch(()=>{
                    this.$message.error('接口请求失败');
                });


            }
        }
    }
</script>

<style scoped>
    .token{padding: 20px;position: relative}
    .token .token_part{
        margin-top: 60px;
    }
</style>