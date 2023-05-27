<template>
  <div>
    {{ $route.query.name }}
  </div>
  <el-row :gutter="20">
    <el-col :span="4">
      <div class="grid-content ep-bg-purple" />
    </el-col>
    <el-col :span="12">
      <el-tabs v-model="activeName" type="border-card" class="search-tabs" @tab-click="handleClick">
        <el-tab-pane label="全站" name="all">
          <el-card class="box-card" v-for="info, index in searchList" :key="index" shadow="hover">
            <div class="left">
              <router-link :to="{ path: '/articles/' + info.id }">
                <el-image style="width: 200px; height: 100px" :src="info.imgUrl" href="#" fit="scale-down" />
              </router-link>
            </div>
            <div class="right" style="">
              <div class="title"><a href="#">{{ info.title }}</a></div>
              <div class="digest"><a href="#">{{ info.digest }}</a></div>
              <div class="tags">
                <a href="#">
                  <span>{{ info.upvote }} 赞</span>
                </a>
                <a href="#">作者：{{ info.author }}</a>
              </div>
            </div>
          </el-card>
        </el-tab-pane>
      </el-tabs>
    </el-col>
    <el-col :span="4">
      <div class="grid-content ep-bg-purple" />
    </el-col>
    <el-col :span="4">
      <div class="grid-content ep-bg-purple" />
    </el-col>
  </el-row>
</template>

<script setup lang="ts">
// 页面依赖
import { ref, onMounted } from 'vue'
import type { TabsPaneContext } from 'element-plus'
import router from "@/router";
import { useRoute } from 'vue-router';
const route = useRoute();

// API 依赖
import { searchArticlesAPI } from '@/api/articles';

const activeName = ref('all')
const searchList = ref();

const handleClick = (tab: TabsPaneContext, event: Event) => {
  router.push({
    path: '/search', query: {
      word: route.query.word,
      filter1: tab.props.name,
    }
  });
}

function getArticle() {
  searchArticlesAPI(route.query)
    .then((data) => {
      searchList.value = data;
    })
}


onMounted(() => {
  // 加载文章
  getArticle();
});

</script>

<style scoped></style>


<style  lang="scss">
.box-card {
  /* border: solid 1px #e0e0e0; */
  margin-top: 15px;
  display: flex;
  border-radius: 4px;
  border-top: 0;
  border-left: 0;
  border-right: 0;
  margin: 15px;

  .el-card__body {
    display: flex;

  }

  .left {
    display: flex;
    margin-right: 16px;
    padding-top: 2px;

    a {
      img {
        width: 200px;
        height: 100px;
      }
    }

  }

  .right {
    display: flex;
    flex-direction: column;

    .title {

      color: #e0e0e0;
      font-size: 18px;
      font-weight: 500;
      color: #222226;
      overflow: hidden;
      white-space: normal;
      word-break: break-word;
      display: -webkit-box;
      -webkit-box-orient: vertical;
      -webkit-line-clamp: 1;
      line-height: 25px;
      margin-bottom: 4px;
    }

    .digest {
      height: 40px;
      font-size: 14px;
      font-weight: 400;
      color: #555666;
      overflow: hidden;
      white-space: normal;
      word-break: break-word;
      display: -webkit-box;
      -webkit-box-orient: vertical;
      -webkit-line-clamp: 2;
    }

    .tags {
      display: -webkit-box;
      align-items: center;
      margin-top: 10px;
      display: flex;
      -webkit-box-align: center;

      span {
        margin-right: 16px;
      }
    }
  }
}
</style>