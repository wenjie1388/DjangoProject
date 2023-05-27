import { createApp } from 'vue';
import router from '@/router';
import App from './App.vue';


import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import './style.css';

const app = createApp(App);


// 全局注册 状态管理(store)
import { setupStore } from '@/store';
setupStore(app);

// 全局挂载
app.use(ElementPlus);
app.use(router);
app.mount('#app');
