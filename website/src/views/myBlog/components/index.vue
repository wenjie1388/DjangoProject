<template>
  <el-row :gutter="20">
    <el-col :span="12">
      <el-card class="user-card1">
        <div class="user-item">
          <span>{{ userCard.upvote }}</span>
          <p>点赞量</p>
        </div>
        <div>
          <span>{{ userCard.pageviews }}</span>
          <p>阅读量</p>
        </div>
        <div>
          <span>{{ userCard.count }}</span>
          <p>篇幅</p>
        </div>
        <div>
          <span>{{ userCard.collect }}</span>
          <p>收藏量</p>
        </div>
      </el-card>

    </el-col>
    <el-col :span="6">
      <div class="grid-content ep-bg-purple" />
    </el-col>
  </el-row>
</template>

<script setup lang="ts">
// 系统依赖
import { ref, onMounted, reactive } from 'vue';

import { getUserInfo } from '@/api/user';

import { useUserStore } from '@/store/modules/user';
const userStore = useUserStore();


// 
const userCard = reactive({
  id: "",
  nickname: "",
  avatar: "",
  upvote: 0,
  pageviews: 0,
  count: 0,
  collect: 0
});

function initUserCard() {
  getUserInfo('v2', '01040203', userStore.id)
    .then((data) => {
      userCard.id = data.id;
      userCard.nickname = data.nickname;
      userCard.avatar = data.avatar;
      userCard.upvote = data.upvote;
      userCard.pageviews = data.pageviews;
      userCard.count = data.count;
      userCard.collect = data.collect;

    })
}

onMounted(() => {
  // 初始化用户的卡片信息
  initUserCard();
});

</script>

<style lang="scss">
.user-card1 {
  text-align: center;

  .el-card__body {
    display: flex;
    gap: 190px;
  }
}
</style>