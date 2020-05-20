import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    maintheme: 'light',
    token: localStorage.getItem('token') ? localStorage.getItem('token') : '',
    mail: localStorage.getItem('mail')? localStorage.getItem('mail'): '',
  },
  mutations: {
    updateToken(state,data){
      state.token = data["token"];
      state.mail = data["mail"];
      window.localStorage.setItem('token',data["token"]);
      window.localStorage.setItem('mail',data["mail"]);
    }
  },
  actions: {
  },
  modules: {
  }
})
