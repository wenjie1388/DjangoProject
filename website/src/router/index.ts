import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router';


// 静态路由
export const constantRoutes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('@/views/index.vue'),
    meta: { auth: false },
  },
  {
    path: '/course',
    component: () => import('@/views/course/index.vue'),
    meta: { auth: false },
  },
  {
    path: '/login',
    component: () => import('@/views/login/index.vue'),
    meta: { auth: false },
  },
  {
    path: '/register',
    component: () => import('@/views/register/index.vue'),
    meta: { auth: false },
  },
  
  {
    path: '/search',
    component: () => import('@/views/search/index.vue'),
    props: route => ({ query: route.query.q })
  },
  {
    // 阅读文章
    path: '/articles/:id',
    component: () => import('@/views/articles/index.vue'),
    meta: { auth: false },
  },
  {
    // 用户中心
    path: '/user-center/:id/',
    name:'userCenter',
    component: () => import('@/views/userCenter/index.vue'),
    redirect: { name: 'profile'},
    meta: { auth: true },
    children: [
      {
        path: 'profile',
        name: 'profile',
        component: () => import('@/views/userCenter/components/profile/index.vue'),
        alias: ['']
      },
      {
        path: 'account',
        name: "account",
        component: () => import('@/views/userCenter/components/account/index.vue'),
        meta: { auth: true },
      },
      {
        path: 'history',
        name: "history",
        component: () => import('@/views/userCenter/components/history/index.vue'),
        meta: { auth: true },
      },
      {
        path: 'setting',
        name: "setting",
        component: () => import('@/views/userCenter/components/setting/index.vue'),
        meta: { auth: true },
      },
    ],
  },
  {
    // 内容管理
    path: '/my-blog/:id',
    name:'myBlog',
    component: () => import('@/views/myBlog/index.vue'),
    meta: { auth: true },
    redirect: { name: 'home'},
    children: [
      {
        path: 'home',
        name: 'home',
        component: () => import('@/views/myBlog/components/index.vue'),
      },
      
      {
        path: 'edit',
        name: 'edit',
        component: () => import('@/views/myBlog/components/edit/index.vue'),
        props: route => ({ query: route.query.q }),

      },
      {

        path: 'content',
        name: 'content',
        component: () => import('@/views/myBlog/components/content/index.vue'),
      },
      {
        path: 'comment',
        name: 'comment',
        component: () => import('@/views/myBlog/components/comment/index.vue'),
      },
      {
        path: 'allColumnList',
        name: 'allColumnList',
        component: () => import('@/views/myBlog/components/allColumnList/index.vue'),
      },
    ]
  },
  
  {
    path: '/blog/:uid',
    name:'blog',
    component: () => import('@/views/blog/index.vue'),
    meta: { auth: false },
  },
  {
    path: '/404',
    name:'404',
    component: () => import('@/views/error-page/404.vue'),
    meta: { auth: false },
  },

  
// {
  //   path: '/redirect',
  //   component: Layout,
  //   meta: { hidden: true },
  //   children: [
  //     {
  //       path: '/redirect/:path(.*)',
  //       component: () => import('@/views/redirect/index.vue')
  //     }
  //   ]
  // },
  // 外部链接
  /*{
        path: '/external-link',
        component: Layout,
        children: [
            {
                path: 'https://www.cnblogs.com/haoxianrui/',
                meta: { title: '外部链接', icon: 'link' }
            }
        ]
    }*/
  // 多级嵌套路由
  /* {
         path: '/nested',
         component: Layout,
         redirect: '/nested/level1/level2',
         name: 'Nested',
         meta: {title: '多级菜单', icon: 'nested'},
         children: [
             {
                 path: 'level1',
                 component: () => import('@/views/nested/level1/index.vue'),
                 name: 'Level1',
                 meta: {title: '菜单一级'},
                 redirect: '/nested/level1/level2',
                 children: [
                     {
                         path: 'level2',
                         component: () => import('@/views/nested/level1/level2/index.vue'),
                         name: 'Level2',
                         meta: {title: '菜单二级'},
                         redirect: '/nested/level1/level2/level3',
                         children: [
                             {
                                 path: 'level3-1',
                                 component: () => import('@/views/nested/level1/level2/level3/index1.vue'),
                                 name: 'Level3-1',
                                 meta: {title: '菜单三级-1'}
                             },
                             {
                                 path: 'level3-2',
                                 component: () => import('@/views/nested/level1/level2/level3/index2.vue'),
                                 name: 'Level3-2',
                                 meta: {title: '菜单三级-2'}
                             }
                         ]
                     }
                 ]
             },
         ]
     }*/
];

// 创建路由
const router = createRouter({
  history: createWebHashHistory(),
  routes: constantRoutes as RouteRecordRaw[],
  // 刷新时，滚动条位置还原
  scrollBehavior: () => ({ left: 0, top: 0 })
});

// 重置路由
export function resetRouter() {
  const permissionStore = usePermissionStoreHook();
  permissionStore.routes.forEach(route => {
    const name = route.name;
    if (name && router.hasRoute(name)) {
      router.removeRoute(name);
    }
  });
}

export default router;
