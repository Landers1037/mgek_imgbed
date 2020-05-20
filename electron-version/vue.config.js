module.exports = {
  productionSourceMap: false,
  css: {
    extract: true
  },
  pluginOptions: {
    electronBuilder: {
      builderOptions: {
        // options placed here will be merged with default configuration and passed to electron-builder
        appId: "liaorenj@gmail.com.mgek_imgbed",
        productName: "mgek_imgbed",
        //icon: "./utils/favicon.ico",
        nsis:{
          oneClick: false,
          allowToChangeInstallationDirectory: true,
          runAfterFinish: false,
          shortcutName: "Mgek_ImgBed",
        },
        extraFiles:[
        ]
      }
    }
  },
  devServer: {
    port: 8080,
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
        ws: false,
        pathRewrite: {
          '^/api': '/api'
        },
      },

    },
  },
};