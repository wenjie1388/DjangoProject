<template>
  <el-row>
    <el-col :span="24">
      <!-- 占位 -->
      <div class="grid-content ep-bg-purple-dark" />
    </el-col>
  </el-row>

  <el-row :gutter="20">
    <el-col :span="16" :offset="4">
      <el-card class="user-e-card">
        <el-row :gutter="20" class="card">
          <el-col :span="4">
            <el-avatar :size="150" class="avatar" :src="usercard.avatar" />
          </el-col>
          <el-col :span="20">
            <div>
              <el-text truncated class="nick">
                {{ usercard.nickname }}
              </el-text>
            </div>
            <div class="" style="gap: 20px;display: flex;">
              <span>{{ usercard.upvote }}赞</span>
              <span>{{ usercard.collect }}收藏</span>
              <span>{{ usercard.pageviews }}访问量</span>
            </div>
            <div class="box-introduction">
              <p class="introduction">
                {{ usercard.introduction }}
              </p>
            </div>
          </el-col>
        </el-row>
      </el-card>
    </el-col>
  </el-row>

  <el-row>
    <el-col :span="16" :offset="4">
      <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
        <el-tab-pane label="文章" name="article">
          <el-card class="article-guide-card" v-for="info in articleGuide" :key="info.id">
            <el-row :gutter="0">
              <el-col :span="4">
                <el-image :src="info.imgUrl" fit="contain" />
              </el-col>
              <el-col :span="19" class="article-info">
                <div><el-text class="title" truncated size="50">
                    <router-link :to="{ path: '/articles/' + route.params.uid }"> {{ info.title }}</router-link>
                  </el-text></div>
                <div class="box-digest">
                  <p class="digest" truncated>
                    {{ info.digest }}
                  </p>
                </div>
                <div class="item " style="display: flex; gap: 15px; ">
                  <span class="upvote">{{ info.upvote }}&nbsp;赞</span>
                  <span><b>|</b> </span>
                  <span class="pageviews">{{ info.pageviews }}&nbsp;阅读量</span>
                  <span><b>|</b> </span>
                  <span class="collect">{{ info.collect }}&nbsp;收藏</span>
                </div>
              </el-col>
            </el-row>
          </el-card>
        </el-tab-pane>
      </el-tabs>
    </el-col>
  </el-row>
</template>

<script setup lang="ts">
// 页面依赖
import { ref, onMounted, reactive, toRefs } from 'vue';
import type { TabsPaneContext } from 'element-plus';
import { Search } from '@element-plus/icons-vue';
import { useRoute } from 'vue-router';
const route = useRoute();


// API依赖
import { ArticleGuide6API, searchArticlesAPI } from '@/api/articles';
import { getUserInfo } from '@/api/user';


// 状态管理依赖
import { useUserStore } from "@/store/modules/user";
const userStore = useUserStore();

// 数据类型依赖
import { userCardType } from "@/api/user/types";

// 声明初值
const search = ref('');
const articleGuide = ref();
const activeName = ref('article');

const state = reactive({
  usercard: {} as userCardType
});

const {
  usercard,
} = toRefs(state);



const handleClick = (tab: TabsPaneContext, event: Event) => {
  console.log(tab, event)
};




// 初始化文章导读
function InitArticleGuide() {
  ArticleGuide6API(route.params.uid)
    .then((data) => {
      articleGuide.value = data;
    })
};

function InitECard() {
  getUserInfo('v2', '01040203', route.params.uid)
    .then((data) => {
      state.usercard = data;
    })

}

onMounted(() => {
  // 初始化文章导读
  InitArticleGuide();
  // 初始化名片
  InitECard();
})
</script>


<style scoped lang="scss">
.user-e-card {
  .nick {
    font-size: 20px;
    font-weight: 600;
  }

  .introduction {
    /*没置文本行数为3行*/
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    /*没置超出部分显示省略号 */
    overflow: hidden;
    text-overflow: ellipsis;
    margin-top: 10px;
  }

}

.el-card__body {


  .article-info {
    padding-left: 15px;
  }

  .article-image {
    max-height: 100px;
    min-height: 100px;
    max-width: 200px;
    min-width: 200px;
  }

  .box-digest {
    min-height: 50px;
  }

  .digest {
    /*没置文本行数为2行*/
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    /*没置超出部分显示省略号 */
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .title {
    font-size: 20px;
    color: #222226;
  }

  .title:hover {
    color: black;
    text-decoration: underline;
  }

  /**
none	默认。定义标准的文本。
underline	定义文本下的一条线。
overline	定义文本上的一条线。
line-through	定义穿过文本下的一条线。
blink	定义闪烁的文本。
inherit	规定应该从父元素继承 text-decoration 属性的值
*/

  p {
    margin: 0;
  }
}
</style>