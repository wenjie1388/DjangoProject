

<template>
  <div :class="{ 'has-logo': sidebarLogo }">
    <logo v-if="sidebarLogo" :collapse="isCollapse" />
    <el-scrollbar>
      <el-menu :default-active="activeMenu" :collapse="isCollapse" :background-color="variables.menuBg"
        :text-color="variables.menuText" :active-text-color="variables.menuActiveText" :unique-opened="false"
        :collapse-transition="false" mode="vertical" router>
        <el-menu-item>
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
        </el-sub-menu>
      </el-menu>
    </el-scrollbar>
  </div>
</template>

<script setup lang="ts">
import { computed, reactive } from 'vue';
import { useRoute } from 'vue-router';
import { HomeFilled, UserFilled, Platform } from '@element-plus/icons-vue';
import Logo from './Logo.vue';
import variables from '@/styles/variables.module.scss';

import { useSettingsStore } from '@/store/modules/settings';
// import { usePermissionStore } from '@/store/modules/permission';
import { useAppStore } from '@/store/modules/app';
import { storeToRefs } from 'pinia';

const settingsStore = useSettingsStore();
// const permissionStore = usePermissionStore();
const appStore = useAppStore();
const { sidebarLogo } = storeToRefs(settingsStore);
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
</script>
