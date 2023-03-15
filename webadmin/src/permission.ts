import router from '@/router';
import { RouteRecordRaw } from 'vue-router';
import { useUserStoreHook } from '@/store/modules/user';

import NProgress from 'nprogress';
import 'nprogress/nprogress.css';
NProgress.configure({ showSpinner: false }); // 进度条


// 白名单路由
const whiteList = ['/login'];

router.beforeEach(async (to, from, next) => {
  NProgress.start();
  const userStore = useUserStoreHook();
  if (userStore.token) {
    // 登录成功，跳转到首页
    if (to.path === '/login') {
      NProgress.done();
      next( '/' );
    } else {
      // const { active } = await userStore.getInfo(userStore.id);
      const active = true
      console.log('userStore', userStore);
      if (active == true) {
        next();
      } else {
        // 移除 token 并跳转登录页
        await userStore.resetToken();
        // next(`/login?redirect=${to.path}`);
        next(`/login`);
        NProgress.done();
      }
    }
  } else {
    // 未登录可以访问白名单页面
    if (whiteList.indexOf(to.path) !== -1) {
      next();
    } else {
      next(`/login`);
      NProgress.done();
    }
  }
});

router.afterEach(() => {
  NProgress.done();
});
