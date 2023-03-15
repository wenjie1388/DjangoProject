<template>
  <el-container>
    <el-aside width="200px">
      <el-menu :default-active="activeIndex2" :collapse="isCollapse" class="usercenter-menu-vertical" @open="handleOpen"
        @close="handleClose" router>
        <el-menu-item-group title="管理首页">
          <el-sub-menu index="1">
            <template #title>发布</template>
            <el-menu-item index="" disabled>文章</el-menu-item>
            <el-menu-item index="" disabled>视频</el-menu-item>
          </el-sub-menu>
        </el-menu-item-group>
        <el-sub-menu index="2">
          <template #title>文章</template>
          <!-- <el-menu-item index="/user/article">文章管理</el-menu-item> -->
          <el-menu-item index="" disabled>评论管理</el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="3">
          <template #title>视频</template>
          <el-menu-item index="" disabled>视频管理</el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="4">
          <template #title>个人中心</template>
          <el-menu-item index="/admin/wenjie/userInfo">基本资料</el-menu-item>
          <el-menu-item index="/admin/wenjie/accountInfo">账号信息</el-menu-item>
          <el-menu-item index="" disabled>隐私设置</el-menu-item>
          <el-menu-item index="" disabled>信息认证</el-menu-item>
          <el-menu-item index="" disabled>我的收藏</el-menu-item>
          <!-- {{ router.currentRoute.path }} -->
        </el-sub-menu>
      </el-menu>
    </el-aside>
    <el-main>
      <RouterView></RouterView>
    </el-main>
  </el-container>
</template>

<script setup lang="ts">
import { ref } from "vue";
import {
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from '@element-plus/icons-vue'
import router from "../../router";

console.log(router.currentRoute)

const isCollapse = ref(false)
const activeIndex2 = ref("/user/article")
// router.currentRoute
const handleOpen = (key: string, keyPath: string[]) => {
  // console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  // console.log(key, keyPath)
  // activeIndex2.value = key
}
</script>

<style scoped>
.usercenter-menu-vertical {
  height: 70vw;
}
</style>