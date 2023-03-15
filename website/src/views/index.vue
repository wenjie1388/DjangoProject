<template>
  <el-row :gutter="20">
    <el-col :span="4" :offset="4">
      <!-- 博主卡片 -->
      <div class="grid-content">
        <Login />
      </div>
    </el-col>
    <el-col :span="8">
      <div class="grid-content ">
        <!-- 文章 -->
        <Activle />
      </div>
    </el-col>
    <el-col :span="4">
      <div class="grid-content ep-bg-purple">{{ $route.params.username }}</div>
    </el-col>
  </el-row>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import Login from '../components/login/index.vue';
import Activle from '../components/article/index.vue'
</script>

<style scoped>
.el-row {
  margin-bottom: 20px;
}

.el-row:last-child {
  margin-bottom: 0;
}

.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
</style>