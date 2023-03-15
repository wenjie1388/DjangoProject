<script setup lang="ts">
import { computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { ElMessageBox } from 'element-plus';

import Hamburger from '@/components/Hamburger/index.vue';
import Breadcrumb from '@/components/Breadcrumb/index.vue';
import Screenfull from '@/components/Screenfull/index.vue';
import SizeSelect from '@/components/SizeSelect/index.vue';
import LangSelect from '@/components/LangSelect/index.vue';
import MixNav from './Sidebar/MixNav.vue';
import { CaretBottom } from '@element-plus/icons-vue';

import { useAppStore } from '@/store/modules/app';
import { useTagsViewStore } from '@/store/modules/tagsView';
import { useUserStore } from '@/store/modules/user';
import { useSettingsStore } from '@/store/modules/settings';

const appStore = useAppStore();
const tagsViewStore = useTagsViewStore();
const userStore = useUserStore();
const settingsStore = useSettingsStore();

const route = useRoute();
const router = useRouter();

const device = computed(() => appStore.device);

function toggleSideBar() {
  appStore.toggleSidebar(true);
}

function logout() {
  ElMessageBox.confirm('确定注销并退出系统吗？', '提示', {
    confirmButtonText: '确定',
    cancelButtonText: '取消',
    type: 'warning'
  }).then(() => {
    userStore
      .logout()
      .then(() => {
        tagsViewStore.delAllViews();
      })
      .then(() => {
        router.push(`/login?redirect=${route.fullPath}`);
      });
  });
}
</script>

<template>
  <div class="navbar">
    <div class="flex justify-start" v-if="device === 'mobile' || settingsStore.layout === 'left'">
      <hamburger :is-active="appStore.sidebar.opened" @toggleClick="toggleSideBar" />
      <!-- 面包屑导航栏 -->
      <breadcrumb />
    </div>

    <div v-if="device === 'mobile' || settingsStore.layout === 'left'" class="navbar-right">
      <el-dropdown trigger="click">
        <div style="justify-content: center;align-items: center;display: flex;margin-left: 0.5rem;
            margin-right: 0.5rem;">
          <img src="https://s2.loli.net/2022/04/07/gw1L2Z5sPtS8GIl.gif?imageView2/1/w/80/h/80"
            class="w-[40px] h-[40px] rounded-lg" style="height: 40px;" />
          <CaretBottom class="w-3 h-3" />
        </div>

        <template #dropdown>
          <el-dropdown-menu>
            <router-link to="/">
              <el-dropdown-item>{{ $t('navbar.dashboard') }}</el-dropdown-item>
            </router-link>
            <a target="_blank" href="https://github.com/hxrui">
              <el-dropdown-item>Github</el-dropdown-item>
            </a>
            <a target="_blank" href="https://gitee.com/haoxr">
              <el-dropdown-item>{{ $t('navbar.gitee') }}</el-dropdown-item>
            </a>
            <a target="_blank" href="https://www.cnblogs.com/haoxianrui/">
              <el-dropdown-item>{{ $t('navbar.document') }}</el-dropdown-item>
            </a>
            <el-dropdown-item divided @click="logout">
              {{ $t('navbar.logout') }}
            </el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.navbar {
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 0px 2px rgba(0, 0, 0, 0.2);
}

.navbar-right {
  display: flex;
}

.el-dropdown {
  --el-dropdown-menu-box-shadow: var(--el-box-shadow-light);
  --el-dropdown-menuItem-hover-fill: var(--el-color-primary-light-9);
  --el-dropdown-menuItem-hover-color: var(--el-color-primary);
  --el-dropdown-menu-index: 10;
  display: inline-flex;
  position: relative;
  color: var(--el-text-color-regular);
  font-size: var(--el-font-size-base);
  line-height: 1;
  vertical-align: top;
}

.leading-\[50px\] {
  line-height: 50px;
}

.px-\[15px\] {
  padding-left: 15px;
  padding-right: 15px;
}

.cursor-pointer {
  cursor: pointer;
}

.h-\[50px\] {
  height: 50px;
}

.el-breadcrumb {
  font-size: 14px;
  line-height: 1;
}

.flex {
  display: flex;
}

.el-breadcrumb {
  font-size: 14px;
  line-height: 1;
}

.h-\[50px\] {
  height: 50px;
}

.cursor-pointer {
  cursor: pointer;
}

.leading-\[50px\] {
  line-height: 50px;
}


.el-dropdown {
  font-size: 18px;
}

.justify-center {
  justify-content: center;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.justify-center {
  justify-content: center;
}

.items-center {
  align-items: center;
}

.flex {
  display: flex;
}

.mx-2 {
  margin-left: 0.5rem;
  margin-right: 0.5rem;
}

img,
svg {
  display: inline-block;
}
</style>
