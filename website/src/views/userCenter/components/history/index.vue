<template>
  <el-timeline>
    <el-timeline-item v-for="info in initHistory" :timestamp="info.date_time" placement="top">
      <el-card>
        <h4>
          <RouterLink :to="{ path: '/articles/' + info.id }">{{ info.title }}</RouterLink>
        </h4>
        <p>{{ info.author }}</p>
      </el-card>
    </el-timeline-item>
  </el-timeline>
</template>

<script setup lang="ts">
// 01040204

// 页面依赖
import { useUserStore } from '@/store/modules/user';
import { ref, onMounted, reactive, computed } from 'vue';
const userStore = useUserStore();

// API 依赖
import { getUserInfo } from '@/api/user';


const initHistory = ref();

function InitBrowsingHistory() {
  getUserInfo('v1', '01040204', userStore.id)
    .then((data) => {
      initHistory.value = data;
    })
};


onMounted(() => {
  // 初始化历史记录
  InitBrowsingHistory();
});

</script>

<style scoped></style>