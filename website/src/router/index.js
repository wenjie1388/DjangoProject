import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      redirect:'/users/wenjie',
      component: () => import('../views/index.vue')
    },
    {
      path: '/users/:username',
      name: 'users',
      component: () => import('../views/index.vue'),
    },
    {
      path: '/admin/:username',
      name: 'admin',
      redirect:'/admin/:username/userInfo',
      component: () => import('../views/admin/index.vue'),
      children:[
        // 用户个人资料页
        {
        path:'userInfo',
        component:()=>import("../components/users/userInfo.vue"),
        },
        // 用户账号信息页
        {
        path:'accountInfo',
        name:'account',
        component:()=>import("../components/users/accountInfo.vue"),
        },
        // 用户博文页
        // {
        // path:'article',
        // name:'article',
        // component:()=>import("../components/users/Article.vue"),
        // }
      ],
    },
    {
      path: '/login',
      name: 'login',
      // redirect:'/',
      component: () => import('../views/login/index.vue')
    },
  ]
})

export default router
