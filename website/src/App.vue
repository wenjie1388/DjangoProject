<template>
  <el-container>
    <el-header style="width: 100%;">
      <el-menu :default-active="appStore.navI" class="el-menu-demo" mode="horizontal" :ellipsis="false"
        @select="handleSelect">
        <div class="logo-box" style="display: flex;margin: auto 0;">
          <h3>LOGO</h3>
          <!-- <el-image style="width: 100px; height: 58px;display: flex;"
            src="https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg" fit="contain" /> -->
        </div>
        <el-menu-item index="/">首页</el-menu-item>
        <!-- <el-menu-item index="bbs">社区</el-menu-item> -->
        <!-- <el-menu-item index="/course">课程</el-menu-item> -->
        <div class="flex-grow" style="display: flex">
          <el-input v-model.trim="input1" size="large" @keyup.enter.native="toSearch()" placeholder="Please Input"
            :suffix-icon="Search" />
        </div>
        <el-menu-item index="login" v-if="userStore.id == ''">登录/注册</el-menu-item>
        <el-sub-menu index="user" v-else>
          <template #title>{{ userStore.nickname }}</template>
          <router-link class="user-box" :to="{ name: 'userCenter', params: { id: userStore.id } }"> 个人中心</router-link>
          <router-link class="user-box" :to="{ name: 'myBlog', params: { id: userStore.id } }"> 内容管理 </router-link>
          <router-link class="user-box" :to="{ path: '/' }" @click="exit">退出</router-link>
        </el-sub-menu>
      </el-menu>
    </el-header>
    <el-main style="width: 100%;background: #FAFAFA;height: 100%;min-height: 1080px;">
      <router-view />
    </el-main>
    <div style="width: 100%;text-align:center">
    </div>
  </el-container>
</template>

<script setup lang="ts">
import { ref, onMounted, onUpdated } from "vue";
import { Search } from "@element-plus/icons-vue";
import { ElMessage } from 'element-plus'

// cookie 依赖
import { getId, getToken } from "@/utils/auth";

// 状态管理依赖
import { useUserStore } from "@/store/modules/user";
import { useAppStore } from "@/store/modules/app";
const userStore = useUserStore();
const appStore = useAppStore();

// 路由管理依赖
import { useRoute } from 'vue-router'
import router from "@/router";
const route = useRoute();

// API 依赖
import { getCarouselAPI } from "@/api/media/index";
import { exitApi } from "@/api/auth/index";

const isLogin = ref(false);
const input1 = ref('');
const handleSelect = (key: string, keyPath: string[]) => {
  appStore.navI = key;
  router.push(key);
};

async function initUser() {
  if (!getToken()) {
    isLogin.value = false;
    userStore.status = true;
  } else {
    userStore
      .getInfo()
      .then(() => {
        isLogin.value = true;
      })
  };
};

const getCarousel = async () => {
  getCarouselAPI()
    .then((data) => {
      return data
    })
};

function toSearch() {
  if (input1.value == '') {
    router.push('/');
  } else {
    router.push({
      path: '/search', query: {
        word: input1.value,
        filter1: 'all',
      }
    });
  }
};

function exit() {
  exitApi(userStore.id)
    .then(() => {
      userStore.resetUser();
      ElMessage.success('已退出');
    })
};


onMounted(() => {
  // 初始化用户
  initUser();

  // 初始化轮播图
  getCarousel();


});
</script>

<style scoped>
.flex-grow {
  flex-grow: 1;
}

.user-box {
  color: #000;
  display: block;
  text-align: center;
  font-size: 15px;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  line-height: 40px;
}
</style>
