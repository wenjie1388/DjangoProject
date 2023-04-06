<template>
  <el-container>
    <el-header style="width: 100%;">
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :ellipsis="false"
        @select="handleSelect" router>
        <div class="logo-box" style="display: flex;">
          <el-image style="width: 100px; height: 58px;display: flex;"
            src="https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg" fit="contain" />
        </div>
        <el-menu-item index="/">首页</el-menu-item>
        <el-menu-item index="bbs">社区</el-menu-item>
        <el-menu-item index="3">课程</el-menu-item>
        <div class="flex-grow" style="display: flex">
          <el-input v-model="input1" size="large" placeholder="Please Input" :suffix-icon="Search" />
        </div>
        <el-menu-item index="3" v-if="is_login == false">登录/注册</el-menu-item>
        <el-sub-menu index="4" v-if="is_login == true">
          <template #title>wenjie1388</template>
          <el-menu-item index="4-1">个人中心</el-menu-item>
          <el-menu-item index="4-2">内容管理</el-menu-item>
        </el-sub-menu>
      </el-menu>
    </el-header>
    <el-main style="width: 100%;">
      <router-view />
    </el-main>
    <el-footer style="width: 100%;height:auto">
      Footer
    </el-footer>
  </el-container>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { Search } from "@element-plus/icons-vue";
const is_login = false;
const activeIndex = ref("/");
const input1 = "";
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
};
</script>

<style scoped>
.flex-grow {
  flex-grow: 1;
}
</style>
