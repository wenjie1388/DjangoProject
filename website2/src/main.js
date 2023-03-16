import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// import store from './store'
import { setupStore } from './store';


const app = createApp(App)

// 全局挂载 stroe
setupStore(app);

app
  .use(router)
  .mount('#app')
