import Vue from 'vue'
import '@/assets/_main.sass'

import App from './App.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
