import { createApp } from 'vue';
import './style.css';
import router from '@/router';
import App from './App.vue';


const app = createApp(App);


// 全局注册 状态管理(store)
import { setupStore } from '@/store';
setupStore(app);

// 全局挂载
app.use(router);
app.mount('#app');
