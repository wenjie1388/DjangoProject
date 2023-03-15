
<template>
  <div :class="classObj" class="app-wrapper">
    <!-- 手机设备 && 侧边栏 → 显示遮罩层 -->
    <div v-if="classObj.mobile && classObj.openSidebar" @click="handleOutsideClick"></div>

    <div class="sidebar-container">
      <div :class="{ 'has-logo': sidebarLogo }">
        <logo v-if="sidebarLogo" :collapse="isCollapse" />
        <Navright v-if="sidebarLogo" :collapse="isCollapse" />
      </div>
    </div>

    <div :class="{ hasTagsView: showTagsView }" class="main-container">
      <div :class="{ 'fixed-header': fixedHeader }">
        <navbar />
      </div>
      <!--主页面-->
      <app-main />
      <!-- 设置面板 -->
      <RightPanel v-if="showSettings">
        <settings />
      </RightPanel>
    </div>
  </div>
</template>


<script setup lang="ts">
import { computed, reactive, watchEffect } from 'vue';
import { useRoute } from 'vue-router';
import Logo from './components/Sidebar/Logo.vue';

import { useSettingsStore } from '@/store/modules/settings';
// import { usePermissionStore } from '@/store/modules/permission';
import { storeToRefs } from 'pinia';
import { useWindowSize } from '@vueuse/core';
import { AppMain, Settings, Navbar, Navright, TagsView } from './components/index';
import Sidebar from './components/Sidebar/index.vue';
import RightPanel from '@/components/RightPanel/index.vue';
import { DeviceType, useAppStore } from '@/store/modules/app';

const { width } = useWindowSize();

/**
 * 响应式布局容器固定宽度
 *
 * 大屏（>=1200px）
 * 中屏（>=992px）
 * 小屏（>=768px）
 */
const WIDTH = 992;
const appStore = useAppStore();
const settingsStore = useSettingsStore();

const fixedHeader = computed(() => settingsStore.fixedHeader);
const showTagsView = computed(() => settingsStore.tagsView);
const showSettings = computed(() => settingsStore.showSettings);

const classObj = computed(() => ({
  hideSidebar: !appStore.sidebar.opened,
  openSidebar: appStore.sidebar.opened,
  withoutAnimation: appStore.sidebar.withoutAnimation,
  mobile: appStore.device === 'mobile'
}));

watchEffect(() => {
  if (width.value < WIDTH) {
    appStore.toggleDevice('mobile');
    appStore.closeSideBar(true);
  } else {
    appStore.toggleDevice('desktop');

    if (width.value >= 1200) {
      //大屏
      appStore.openSideBar(true);
    } else {
      appStore.closeSideBar(true);
    }
  }
});

function handleOutsideClick() {
  appStore.closeSideBar(false);
}

// const permissionStore = usePermissionStore();

const { sidebarLogo } = storeToRefs(settingsStore);

const isCollapse = computed(() => !appStore.sidebar.opened);

</script>

<style lang="scss" scoped>
@import '@/styles/mixin.scss';
@import '@/styles/variables.module.scss';

.app-wrapper {
  @include clearfix;
  position: relative;
  height: 100%;
  width: 100%;

  &.mobile.openSidebar {
    position: fixed;
    top: 0;
  }
}

.drawer-bg {
  background: #000;
  opacity: 0.3;
  width: 100%;
  top: 0;
  height: 100%;
  position: absolute;
  z-index: 999;
}

.fixed-header {
  position: fixed;
  top: 0;
  right: 0;
  z-index: 9;
  width: calc(100% - #{$sideBarWidth});
  transition: width 0.28s;
}

.hideSidebar .fixed-header {
  width: calc(100% - 54px);
}

.mobile .fixed-header {
  width: 100%;
}

.flex {
  display: flex;
}

.h-\[50px\] {
  height: 50px;
}

div {
  display: block;
}
</style>
