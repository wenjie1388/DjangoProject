<template>
  <!-- <el-row :gutter="14">
    <el-col :span="12" :offset="2">
      <div class="carousel-box grid-content" style="margin-left: 0px;">
        <el-carousel>
          <el-carousel-item v-for="user, index in carousels" :key="index">
            <el-image style="width:940px; height: 300px" :src="user.imgurl" fit="scale-down" />
          </el-carousel-item>
        </el-carousel>
      </div>
    </el-col>
    <el-col :span="6" style=" padding-top: 5px;">
    </el-col>
  </el-row> -->
  <!-- 
  <el-row :gutter="14">
    <el-col :span="12" :offset="2">
      <el-tabs v-model="activetabs" class="demo-tabs" @tab-click="handleClick">
        <el-tab-pane label="推荐" name="Recommend">
          <el-card class="box-card" v-for="user, index in recommendedList" :key="index" shadow="hover"
            v-infinite-scroll="getRecommendedAritcle" :infinite-scroll-disabled="redisabled">
            <div class="left">
              <router-link :to="{ path: '/articles/' + user.id }">
                <el-image style="width: 200px; height: 100px" :src="user.imgUrl" href="#" fit="scale-down" />
              </router-link>
            </div>
            <div class="right" style="">
              <div class="title"><router-link :to="{ path: '/articles/' + user.id }">{{ user.title }}</router-link></div>
              <div class="digest"><router-link :to="{ path: '/articles/' + user.id }">{{ user.digest }}</router-link>
              </div>
              <div class="tags">
                <span>{{ user.upvote }} 赞</span>
                <router-link :to="{ path: '/blog/' + user.id }">{{ user.author }}</router-link>
              </div>
            </div>
          </el-card>
        </el-tab-pane>
        <el-tab-pane label="热榜" name="HotList">
          <el-card class="box-card" v-for="user in hotList" :key="user.id" shadow="hover"
            v-infinite-scroll="getHotListAritcle" :infinite-scroll-disabled="infinitedisabled.hot">
            <div class="left">
              <a href="/articles">
                <img :src="user.imgUrl" alt="">
              </a>
            </div>
            <div class="right" style="">
              <div class="title"><router-link :to="{ path: '/articles/' + user.id }">{{ user.title }}</router-link></div>
              <div class="digest"><router-link :to="{ path: '/articles/' + user.id }">{{ user.digest }}</router-link>
              </div>
              <div class="tags">
                <span>{{ user.upvote }} 赞</span>
                <router-link :to="{ path: '/blog/' + user.id }">{{ user.author }}</router-link>
              </div>
            </div>
          </el-card>
        </el-tab-pane>
      </el-tabs>
    </el-col>
    <el-col :span="6">

<el-card class="activity-card">
        <template #header>
          <div class="card-header">
            <b>推荐活动</b>
            <a href="#" style="float: right;">更多活动</a>
          </div>
        </template>
        <div v-for="user in recommendedActivity" :key="user.id" class="activity-item">
          <router-link to="#">
            <span>{{ user.title }} </span>
            <el-icon>
              <ArrowRightBold />
            </el-icon>
          </router-link>
        </div>
      </el-card>
  </el-col>
  </el-row>  -->
</template>

<script lang="ts" setup>
// 页面依赖
import { ref, onMounted, reactive, computed } from 'vue';
import type { TabsPaneContext, } from 'element-plus';
import { Pointer, ArrowRightBold } from '@element-plus/icons-vue';

// cookie 依赖
import { getId, getToken } from "@/utils/auth";

// 状态管理依赖
import { useUserStore } from "@/store/modules/user";
const userStore = useUserStore();

// API 依赖
import { getCarouselAPI } from "@/api/media/index";
import { ArticlesAPI, HotNewsAPI } from "@/api/articles/index";
import { getActivityRecommendationApi } from "@/api/activity/index";

// 数据类型依赖

const infinitedisabled = reactive({
  recommend: false,
  hot: true
})


// const noMore = computed(() => recommendedList >= 20);
const loading = ref(false);
const redisabled = ref(true);
const activetabs = ref('Recommend');

// 定义走马灯
const carousels = ref();
// 定义推荐文章
const recommendedList = ref();
// 定义热门文章
const hotList = ref();
// 定义热门新闻
const hotnews = ref();
// 定义推荐活动
const recommendedActivity = ref();



const handleClick = (tab: TabsPaneContext, event: Event) => {
  // console.log(tab, event)
}

// 推荐文章
function getRecommendedAritcle() {
  redisabled.value = false;
  setTimeout(() => {
    ArticlesAPI('03010101').then(async (data) => {
      recommendedList.value += data;
      infinitedisabled.recommend = true;
    });
  }, 2000)
}


// 热榜文章
function getHotListAritcle() {
  infinitedisabled.hot = false;
  ArticlesAPI('03010102').then((data) => {
    hotList.value += data;
    infinitedisabled.hot = true;
  });
};


// 走马灯
function InitCarousel() {
  getCarouselAPI().then((data) => {
    carousels.value = data;
  });
}

// 热点新闻
function InitHotNews() {
  HotNewsAPI()
    .then((data) => {
      hotnews.value = data;
    })
}

// 推荐文章
function InitRecommendedAritcle() {
  ArticlesAPI('03010101')
    .then(async (data) => {
      recommendedList.value = data;
    });
}

// 热榜文章
function InitHotListAritcle() {
  ArticlesAPI('03010102')
    .then((data) => {
      hotList.value = data;
    });
};

// 活动推荐
function InitActivityRecommendationApi() {
  getActivityRecommendationApi()
    .then((data) => {
      recommendedActivity.value = data;
    })
};


onMounted(() => {
  // 初始化轮播图
  // InitCarousel();
  // 初始化热点
  // InitHotNews();
  // 初始化推荐
  // InitRecommendedAritcle();
  // 初始化热榜
  // InitHotListAritcle();
  // 初始化推荐活动
  // InitActivityRecommendationApi();
})
</script>


<style  lang="scss">
.el-col {
  border-radius: 4px;
}


.news-card {

  .card-header,
  .el-card__header {

    // padding-left: 10px;
    // padding-right: 10px;
    // padding-bottom: 0px;
    // padding-top: 0px;

  }

  .el-card__body {
    padding: 0;


    .text-item {
      display: flex;
      flex-direction: column;
      margin: 10px 15px 10px 15px;

      .news-title {
        font-size: 14px;
        font-weight: 400;
        color: #555666;
        overflow: hidden;
        white-space: normal;
        word-break: break-word;
        display: -webkit-box;
        -webkit-box-orient: vertical;
        -webkit-line-clamp: 1;
      }

      .news-digest {
        font-size: 14px;
        font-weight: 400;
        color: #555666;
        overflow: hidden;
        white-space: normal;
        word-break: break-word;
        display: -webkit-box;
        -webkit-box-orient: vertical;
        -webkit-line-clamp: 1;
      }
    }
  }

}

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

.box-card:hover {
  background-color: #f5f5f5;
}

.activity-card {
  margin-top: 15px;

  .el-card__header {
    padding: 24px;
  }

  .activity-item {
    margin-bottom: 9px;
  }

  span,
  i {
    vertical-align: middle;
  }

  i {
    float: right;
  }

}
</style>
