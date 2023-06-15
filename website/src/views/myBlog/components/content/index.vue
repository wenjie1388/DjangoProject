<template>
  <el-tabs type="content-card">
    <el-tab-pane label="文章">
      <el-row :gutter="10">
        <el-col :span="24" style="padding-bottom: 15px;">
          <el-input v-model.trim="search" @keyup.enter.native="toSearch()" class="w-50 m-2" placeholder="输入关键词"
            :suffix-icon="Search" />
        </el-col>
      </el-row>

      <el-row :gutter="10">
        <el-col :span="24">
          <el-card class="article-guide-card" v-for="info in articleGuide" :key="info.id">
            <el-row :gutter="10">
              <el-col :span="21">
                <el-row :gutter="10">
                  <el-col :span="4">
                    <el-image style="width: 200px; height: 100px" :src="info.imgUrl" fit="contain" />
                  </el-col>
                  <el-col :span="15">
                    <div class="item">{{ info.title }}</div>
                    <div class="item digest">
                      <span>{{ info.digest }}</span>
                    </div>
                    <div class="item " style="display: flex; gap: 15px; ">
                      <span>{{ info.upvote }}&nbsp;赞</span>
                      <span><b>·</b> </span>
                      <span>{{ info.pageviews }}&nbsp;阅读量</span>
                      <span><b>·</b> </span>
                      <span>{{ info.collect }}&nbsp;收藏</span>
                    </div>
                  </el-col>
                </el-row>
              </el-col>
              <el-col :span="3">
                <div class="item" style="text-align: right;">{{ info.create_date }}</div>
                <div class="item action">
                  <RouterLink :to="{ path: '/articles/' + info.id }">浏览</RouterLink>
                  <RouterLink :to="{ path: '/my-blog/' + info.id + '/edit/' }">编辑</RouterLink>
                  <RouterLink to="#">删除</RouterLink>
                </div>
              </el-col>
            </el-row>
          </el-card>
        </el-col>
      </el-row>
    </el-tab-pane>
  </el-tabs>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { Search } from '@element-plus/icons-vue';
import router from '@/router';

// API依赖
import { ArticleGuide6API, searchArticlesAPI } from '@/api/articles';

// 状态管理依赖
import { useUserStore } from "@/store/modules/user";
const userStore = useUserStore();

// 声明初值
const search = ref('');
const articleGuide = ref();

// 搜索动作
function toSearch() {
  if (search.value == '') {
    return
  } else {
    searchArticlesAPI({ "word": search.value })
      .then((data) => {
        articleGuide.value = data;
      })
  }
}


// 初始化文章导读
function InitArticleGuide() {
  ArticleGuide6API(userStore.id)
    .then((data) => {
      articleGuide.value = data;
    })
};

onMounted(() => {
  // 初始化文章导读
  InitArticleGuide();

})
</script>

<style lang="scss" scoped>
.article-guide-card {
  border-top: 0px;
  border-left: 0px;
  border-bottom: 1px solid #ccc;
  border-right: 0px;
  box-shadow: none;
  border-radius: 0px;



}
</style>


<style scoped>
.digest {
  height: 60px;
}

.action {
  padding-top: 60px;
  display: flex;
  gap: 45px;
}
</style>