<template>
  <el-row :gutter="30">
    <el-col :span="4">
    </el-col>
    <el-col :span="4">
      <el-menu :default-active="defaultActive" class="el-menu-vertical" @select="SelectOpen" router>
        <el-menu-item index="profile"><span>个人资料</span></el-menu-item>
        <el-menu-item index="account"><span>账号设置</span></el-menu-item>
        <el-menu-item index="history"><span>浏览历史</span></el-menu-item>
      </el-menu>
    </el-col>
    <el-col :span="12" class="grid-content">
      <router-view />
    </el-col>
    <el-col :span="4">
    </el-col>
  </el-row>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';

// 路由管理依赖
import router from "@/router";

// 状态管理依赖
import { useUserStore } from "@/store/modules/user";
import { useAppStore } from "@/store/modules/app";
const userStore = useUserStore();

// 初始化默认路由
const defaultActive = ref('profile');

const SelectOpen = (key: string, keyPath: string[]) => {
  // '/user-center/' + { $route.params.id } + 'profile'
  const path = '/user-center/' + userStore.id + '/' + key;
  defaultActive.value = key;
  router.push(path);
}

onMounted(() => {
  // 加载
});

</script>


<style>
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.el-menu-vertical {
  border: 0;
}
</style>
