# mgekuni_media
一个restful视频图片管理后端服务，提供html版和electron版本

对原有项目mgek_imghost的重写，分成前后端项目，此项目仅提供后端的api服务

## 实现

基于原生的Flask实现，旨在提供轻量使用简易的图床服务

## 目前功能🔨

1. 图片的上传保存服务，目前支持`jpg`，`png`，`webp`，`gif`格式的图片上传，大小限制为10mb
2. 图片的唯一化存储，默认使用`sqlite`数据库存储图片数据，可以使用配置文件修改为`MongoDB`存储
3. 图片名称安全化处理，无需考虑文件名称是否符合标准，后端会自动生成标准的唯一图片标识。默认使用`base64`编码，可以设置为使用`md5`摘要的方式
4. 接口响应统一格式化，通过封装函数实现JSON响应数据的标准化
5. 标准化的配置文件，JSON格式的配置文件，在服务启动后自动生成，可以根据需求进行修改
6. 原生支持异步IO处理

## 尚未实现🛠

1. Mongo的引擎连接
2. 后端的文件错误类型处理机制优化
3. 视频文件的上传
4. 数据的验证加密，默认只使用`referer`形式验证

## 感谢

感谢**先科**大佬提供技术支持，本项目的测试文件经先科大佬指导完成

感谢先科大佬提供的数据库优化思路

## 配置

### 默认配置

```json
{
  "port": 5000,
  "debug": true,
  "server_name": null,
  "multiroutine": false,
  "server": {
    "image_path": "",
    "image_size": 10485760,
    "image_url": "",
    "image_rule": "base64",
    "image_zip": false,
    "image_zip_path": ""
  },
  "database": {
    "engine": "sqlite",
    "sqlite": "sqlite:///test.db",
    "mongo": ""
  }
}
```

通过配置文件可以自定义服务

`server_name` 服务绑定的域名，在部署到服务器后可以使用

`multiroutine` 是否使用异步IO支持，仅在不使用Server部署时使用

`image_path` 图片的保存地址，绝对路径，为空时系统会自动生成

`image_url` 图片在服务器上的地址，需要在定义域名后使用

`image_rule` 图片的命名规则，使用base64或者md5

`image_zip` 是否开启缩略图

`image_zip_path` 默认的缩略图存储位置，绝对路径

`engine` 使用的数据库类型sqlite或者MongoDB



## 示例

### 错误响应示例

本项目对响应函数进行了封装以实现统一化的响应数据

```json
{
  "data": "图片信息获取失败",
  "type": "error"
}
```

### 正确响应示例

```json
{
  "data": "图片信息获取成功",
  "type": "ok"
}
```

### 成功的图片上传示例

```json
{
  "data": "文件上传成功",
  "type": "ok"
}
```

### 错误的图片上传示例

```json
{
  "data": "空的上传文件",
  "type": "error"
}
```

## 

## 部署

使用WSGI服务或者ASGI服务部署此应用

```python
$ gunicorn -w 2 -b 127.0.0.1:5000 img_server:app
```

具体使用参数参考

[OSChina](https://www.oschina.net/p/gunicorn?hmsr=aladdin1e1)

[Gunicorn](https://gunicorn.org/)

