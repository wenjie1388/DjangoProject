<template>
  <el-menu
    :default-active="activeIndex"
    class="el-menu-demo"
    mode="horizontal"
    :ellipsis="false"
    @select="handleSelect"
  >
    <el-menu-item index="0">LOGO</el-menu-item>
    <el-menu-item index="1">社区</el-menu-item>
    <el-menu-item index="2">课程</el-menu-item>
    <div class="flex-grow" >
        <el-input
      v-model="input1"
      size="large"
      placeholder="Please Input"
      :suffix-icon="Search"
    />
    </div>
    <el-menu-item index="3" v-if='is_login == false'>登录/注册</el-menu-item>
    <el-sub-menu index="4" v-if='is_login == true'>
      <template #title>Workspace</template>
      <el-menu-item index="4-1">item one</el-menu-item>
      <el-sub-menu index="4-2">
        <template #title>item four</template>
        <el-menu-item index="4-2-1">item one</el-menu-item>
      </el-sub-menu>
    </el-sub-menu>
  </el-menu>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { Search } from '@element-plus/icons-vue';
const is_login = false;
const activeIndex = ref('1');
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath);
};
</script>

<style>
.flex-grow {
  flex-grow: 1;
}
</style>
