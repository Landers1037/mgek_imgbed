<template>
    <div class="list">
        <h3>图片列表</h3>
        <p style="color: red;font-size: 12px">暂不支持懒加载</p>
        <i class="el-icon-arrow-left" style="position: absolute;left: 15px;top: 15px;font-weight:bold" @click="home"></i>
        <div class="image_part">
            <div class="img" v-for="i in imagelist" v-bind:key="i.name" @click="show(i.name)">
                <el-image
                        style="width: 100%; height: 100%"
                        :src="i.url"
                        fit="fill">
                    <div slot="error" class="image-slot">
                    <i class="el-icon-picture-outline"></i>
                    </div>
                </el-image>
            </div>
        </div>
        <el-dialog
                title="图片信息"
                :visible.sync="dialogVisible"
                width="90%">
            <p>更新日期{{info.time}}</p>
            <el-image
                    style="width: fit-content; height: auto;max-width: 80%"
                    :src="info.url"
                    fit="fill">
                <div slot="error" class="image-slot">
                    <i class="el-icon-picture-outline"></i>
                </div>
            </el-image>
            <p style="color: crimson">图片信息： {{info.name}}</p>
            <p style="color: #42b983">图片地址： {{info.url}}</p>
            <span slot="footer" class="dialog-footer">
                <el-button type="danger" @click="delete_img">删 除</el-button>
                <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
    export default {
        name: "list",
        data(){
            return{
                dialogVisible: false,
                imagelist:[],
                info: {}
            }
        },
        mounted(){
          this.get_list();
        },
        methods:{
            home(){
                this.$router.push('/home')
            },
            get_list(){
                let _this = this;
                let token = this.$store.state.token;
                _this.$axios.get('/api/image_list?token=' + token).then(res=>{
                    if(res.data.type === 'error'){
                        _this.$message.error('获取图片列表失败')
                    }else{
                        _this.imagelist = res.data.data;
                        _this.$message({type: 'success',message:'刷新列表成功'})
                    }
                }).catch(()=>{
                    _this.$message.error('获取请求失败')
                })
            },
            show(name){
                //目前url对应的不是缩略图就是原图
                let _this = this;
                let token = this.$store.state.token;
                _this.$axios.get('/api/image_info?token=' + token + '&name=' +name).then(res=>{
                    if(res.data.type === 'error'){
                        _this.$message.error('获取图片信息失败');
                    }else{
                        _this.info = res.data.data;
                        console.log(res.data.data);
                        _this.dialogVisible = true;
                    }
                }).catch(()=>{
                    _this.$message.error('获取请求失败');
                })
            },
            delete_img(){
                let name = this.info.name;
                let token = this.$store.state.token;
                let _this = this;
                _this.$axios.post('/api/image_delete?token=' +token,{"name": name}).then(res=>{
                    if(res.data.type === 'error'){
                        _this.$message.error('删除图片失败');
                    }else{
                        _this.$message({type: 'success',message: '图片删除成功'});
                        //清空信息
                        _this.info = {};
                        _this.dialogVisible = false;
                        _this.get_list();
                    }
                }).catch(()=>{
                    _this.$message.error('获取请求失败');
                })
            }
        }
    }
</script>

<style scoped>
    .list{
        padding: 20px 10px 5px 10px;
        position: relative;
    }
    .list .image_part{
        margin-top: 20px;
        border: 1px solid #404040;
        overflow-y: auto;
        height: 425px;
    }
    .image_part .img{
        width: 24%;
        height: auto;
        display: inline-block;
        border: 1px dotted #a0a0a0;
        cursor: pointer;
    }
</style>