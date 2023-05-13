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
        <el-menu-item index="login" v-if="userStore.id == ''">登录/注册</el-menu-item>
        <el-sub-menu index="" v-else>
          <template #title>{{ userStore.nickname }}</template>
          <router-link :to="{ name: 'userCenter', params: { id: userStore.id } }" class="user-box">个人中心</router-link>
          <router-link :to="{ name: 'userCenter', params: { id: userStore.id } }" class="user-box">内容管理</router-link>
        </el-sub-menu>
      </el-menu>
    </el-header>
    <el-main style="width: 100%;background: #FAFAFA;height:500px">
      <router-view />
    </el-main>
    <el-footer style="width: 100%;height: auto;position: absolute;bottom: 0px;text-align:center">
      <div><span>关于我们
          招贤纳士
          商务合作
        </span></div>
    </el-footer>
  </el-container>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { Search } from "@element-plus/icons-vue";


// cookie 依赖
import { getId, getToken } from "@/utils/auth";

// 状态管理依赖
import { useUserStore } from "@/store/modules/user";
import { useAppStore } from "@/store/modules/app";
const userStore = useUserStore();



const isLogin = ref(false);
const activeIndex = ref("/");
const input1 = "";
const handleSelect = (key: string, keyPath: string[]) => {

  // console.log(key, keyPath);
};

async function getUser() {
  if (!getToken()) {
    isLogin.value = false;
    userStore.status = true;
  } else {
    userStore
      .getInfo()
      .then(() => {
        isLogin.value = true;
      })
  }
  console.log('$id:' + userStore.$id, 'id:' + userStore.nickname)
}


onMounted(() => {
  // 初始化用户
  getUser();
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
