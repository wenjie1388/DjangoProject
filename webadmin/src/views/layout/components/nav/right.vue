<template>
  <div>
    <el-menu :default-active="activeMenu" :collapse="isCollapse" :background-color="variables.menuBg"
      :text-color="variables.menuText" :active-text-color="variables.menuActiveText" :unique-opened="false"
      :collapse-transition="false" mode="vertical" @open="handleOpen" @close="handleClose" router>
      <el-menu-item index="/">
        <el-icon>
          <HomeFilled />
        </el-icon>
        <template #title>首页</template>
      </el-menu-item>
      <el-sub-menu index="1">
        <template #title>
          <el-icon>
            <Platform />
          </el-icon>
          <span>系统管理</span>
        </template>
        <el-menu-item index="/user">
          <el-icon>
            <UserFilled />
          </el-icon>
          <span>用户管理</span>
        </el-menu-item>
        <el-menu-item index="/article">
          <el-icon>
            <UserFilled />
          </el-icon>
          <span>博文管理</span>
        </el-menu-item>
      </el-sub-menu>
    </el-menu>
  </div>
</template>

<script setup lang="ts">
import { computed, reactive, watchEffect } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { DeviceType, useAppStore } from '@/store/modules/app';
import variables from '@/styles/variables.module.scss';

import { HomeFilled, UserFilled, Platform } from '@element-plus/icons-vue';

const appStore = useAppStore();
const route = useRoute();
const isCollapse = computed(() => !appStore.sidebar.opened);

const activeMenu = computed<string>(() => {
  const { meta, path } = route;
  if (meta?.activeMenu) {
    return meta.activeMenu as string;
  }
  return path;
});

const routes = reactive([
  { path: '#', },
]);

const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}

const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>

<style scoped  lang="scss">
@import '@/styles/mixin.scss';
@import '@/styles/variables.module.scss';
</style>