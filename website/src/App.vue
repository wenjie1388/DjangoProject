<template>
  <el-container>
    <el-header>
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :ellipsis="false"
        @select="handleSelect" router>
        <div class="flex-grow" />

        <el-menu-item index="/users/wenjie">LOGO</el-menu-item>
        <div class="flex-grow" />
        <el-menu-item index="/users/wenjie">首页</el-menu-item>
        <div class="flex-grow" />
        <!-- <el-menu-item index="/index">文章</el-menu-item> -->
      </el-menu>
    </el-header>
    <el-main>
      <RouterView></RouterView>
    </el-main>
  </el-container>
</template>

<script setup lang="ts">
import { ref, onMounted, reactive } from 'vue'
import Index from './views/Index.vue';
import { loginApi } from './api/auth/index'
import { useUserStore } from './store/modules/user'


const activeIndex = ref('1')
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}


</script>

<style>
.flex-grow {
  flex-grow: 1;
}
</style>
