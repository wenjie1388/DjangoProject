<script lang="ts" setup>
import { ref } from 'vue';
import { useSettingsStore } from '@/store/modules/settings';

const settingsStore = useSettingsStore();

defineProps({
  collapse: {
    type: Boolean,
    required: true
  }
});

const logo = ref<string>(
  new URL(`../../../assets/logo.png`, import.meta.url).href
);
</script>

<template>
  <transition class="w-full h-[50px] bg-gray-800 dark:bg-[var(--el-bg-color-overlay)]">
    <router-link key="expand" class="router-link-active h-full w-full flex items-center justify-center" to="/">
      <el-image v-if="settingsStore.sidebarLogo" class="w-5 h-5" :src="logo" fit="contain" />
      <!-- <img v-if="settingsStore.sidebarLogo" :src="logo" class="w-5 h-5" /> -->
      <span class="ml-3 text-white text-sm font-bold">后台管理系统</span>
    </router-link>
  </transition>
</template>

<style>
.bg-gray-800 {
  --un-bg-opacity: 1;
  background-color: rgba(31, 41, 55, var(--un-bg-opacity));
}

.flex {
  display: flex;
}

.items-center {
  align-items: center;
}

.justify-center {
  justify-content: center;
}

.w-full {
  width: 100%;
}

.h-full {
  height: 100%;
}

.w-5 {
  width: 1.25rem;
}

.h-5 {
  height: 1.25rem;
}

.text-white {
  --un-text-opacity: 1;
  color: rgba(255, 255, 255, var(--un-text-opacity));
}

.font-bold {
  font-weight: 700;
}

.text-sm {
  font-size: .875rem;
  line-height: 1.25rem;
}

.bg-gray-800 {
  --un-bg-opacity: 1;
  background-color: rgba(31, 41, 55, var(--un-bg-opacity));
}

.h-\[50px\] {
  height: 50px;
}
</style>
