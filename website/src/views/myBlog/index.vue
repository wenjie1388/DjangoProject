<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="200px">
        <el-menu :default-active="defaultActive" class="el-menu-vertical-demo" @select="handleSelect" :router="true">
          <el-menu-item index="home">
            <span>首页</span>
          </el-menu-item>
          <el-menu-item index="edit">
            <span>发布文章</span>
          </el-menu-item>
          <el-menu-item index="content">内容管理</el-menu-item>

          <!-- <el-sub-menu index="1">
            <template #title>
              <span>管理</span>
            </template> -->
          <!-- <el-menu-item-group title=""> -->
          <!-- <el-menu-item index="article">内容管理</el-menu-item> -->
          <!-- <el-menu-item index="comment">评论管理</el-menu-item> -->
          <!-- <el-menu-item index="allColumnList">专栏管理</el-menu-item> -->
          <!-- </el-menu-item-group> -->
          <!-- </el-sub-menu> -->
        </el-menu>
      </el-aside>
      <el-main>
        <router-view />

      </el-main>
    </el-container>
  </div>
</template>

<script setup lang="ts">

// 系统依赖
import { ref, onMounted } from 'vue';

// 路由管理依赖
import router from "@/router";

// 状态管理依赖
import { useUserStore } from "@/store/modules/user";
import { useAppStore } from "@/store/modules/app";
const userStore = useUserStore();

const defaultActive = ref('')

const handleSelect = (key: string, indexPath: string, keyPath: string[], item: string, routeResult: string) => {
  // console.log(key, indexPath, keyPath, item, routeResult)
  const path = '/my-blog/' + userStore.id + '/' + key;
  defaultActive.value = key;
  router.push(path);
};


onMounted(() => { });
</script>

<style scoped></style>