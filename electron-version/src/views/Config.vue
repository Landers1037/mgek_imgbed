<template>
    <div class="config">
        <h3>配置文件</h3>
        <i class="el-icon-arrow-left" style="position: absolute;left: 15px;top: 15px;font-weight:bold" @click="home"></i>
        <p style="color: #a0a0a0;font-size: 12px">请先运行后端服务</p>

        <div style="margin-top: 40px">
            <p style="color: #a0a0a0;font-size: 14px;margin-bottom: 6px">将会打开JSON文件，默认使用编辑器打开</p>
            <el-input v-model="input_path" placeholder="手动输入配置文件路径" style="width: 400px;margin-bottom: 10px"></el-input>
            <el-button @click="open" type="primary">打开配置文件</el-button>
        </div>
    </div>
</template>

<script>
    import  {shell} from 'electron';
    export default {
        name: "Config",
        data(){
            return{
                path: '',
                input_path: ''
            }
        },
        methods:{
            home(){
                this.$router.push('/')
            },
            open(){
                let input_path = this.input_path;
                if (input_path) {
                    try {
                        shell.openItem(input_path);
                    } catch (e) {
                        this.$message.error('配置文件打开失败');
                        this.$message('请在输入栏输入绝对路径');
                    }
                }else {
                    //优先获取路径
                    this.get_path();
                }
            },
            get_path(){
                let _this = this;
                this.$axios.get('/api/get_config').then(res=>{
                    if(res.data!==''){
                        _this.path = res.data;
                        try {
                            shell.openItem(res.data);
                        } catch (e) {
                            this.$message.error('配置文件打开失败');
                            this.$message('请在输入栏输入绝对路径');
                        }
                    }
                }).catch((e)=>{
                    console.log(e);
                    this.$message.error('无法从后端获取路径');
                })
            }
        }
    }
</script>

<style scoped>
    .config{
        padding: 20px;
    }
</style>