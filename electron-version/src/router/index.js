import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About'
import Config from '../views/Config'
import home from  '../views/Image/home'
import token from  '../views/Image/token'
import list from "../views/Image/list";

Vue.use(VueRouter);
//在首次运行时记载全部的js文件无需动态路由加载
  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
    {
      path: '/config',
      name: 'Config',
      component: Config
    },
    {
      path: '/home',
      name: 'home',
      component: home
    },
    {
      path: '/token',
      name: 'token',
      component: token
    },
    {
      path: '/image_list',
      name: 'image_list',
      component: list
    },
];

const router = new VueRouter({
  routes
});

export default router
