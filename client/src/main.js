import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.min.css'


Vue.config.productionTip = false
Vue.use(Antd)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
