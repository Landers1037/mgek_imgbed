<template>
    <div class="image_home">
        <h3>上传图片</h3>
        <i class="el-icon-arrow-left" style="position: absolute;left: 15px;top: 15px;font-weight:bold" @click="home"></i>
        <p style="color: #a0a0a0;font-size: 12px;margin-bottom: 10px">注意上传图片需要先获取token</p>
        <el-button type="primary" @click="token">前往生成token</el-button>

        <div class="image_part">
            <el-upload
                    class="upload"
                    :action="url"
                    multiple
                    accept="image/jpeg,image/png,image/gif,image/webp"
                    :limit="10"
                    :on-exceed="handleExceed"
                    :before-remove="beforeRemove"
                    :on-error="error"
                    :on-success="success"
                    :file-list="fileList">
                <el-button size="small" type="primary">点击上传</el-button>
                <div slot="tip" class="el-upload__tip">只能上传jpg/png/webp/gif文件，且不超过10mb</div>
            </el-upload>
        </div>
    </div>
</template>

<script>
    export default {
        name: "home",
        data(){
            return{
                url: this.gen_url(),
                fileList: []
            }
        },
        methods:{
            home(){
                this.$router.push('/')
            },
            token(){
                this.$router.push('/token');
            },
            gen_url(){
                let token = this.$store.state.token;
                return '/api/image_upload?token=' + token;
            },
            handleExceed(files, fileList) {
                this.$message.warning(`当前限制选择 10 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
            },
            beforeRemove(file, fileList) {
                return this.$confirm(`确定移除 ${file.name}？`);
            },
            error(err){
                console.log(err)
            },
            success(s){
                if(s["type"] === "forbidden"){
                    this.$message.error('无上传权限，请先获取token')
                }else{
                    this.$message({type: 'success', message: '上传完成'})
                }
            }
        }
    }
</script>

<style scoped>
    .image_home{
        padding: 20px;
        position: relative;
    }
    .image_home .image_part{
        margin-top: 40px;
        padding: 10px;
    }
</style>