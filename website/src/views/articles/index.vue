<template>
  <el-row :gutter="20">

    <el-col :span="2">
    </el-col>
    <el-col :span="4">
      <el-card class="user-card">
        <el-row :gutter="20" class="user-info">
          <el-col :span="6">
            <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png" />
          </el-col>
          <el-col :span="12">
            <div>{{ author.nickname }}</div>
          </el-col>
        </el-row>

        <el-row :gutter="10">
          <el-col :span="6" class="user-item">
            <div>{{ author.count }}</div>
            <div>篇数</div>
          </el-col>
          <el-col :span="6" class="user-item">
            <div>{{ author.pageviews }}</div>
            <div>阅读量</div>
          </el-col>
          <el-col :span="6" class="user-item">
            <div>{{ author.upvote }}</div>
            <div>点赞</div>
          </el-col>
          <el-col :span="6" class="user-item">
            <div>{{ author.collect }}</div>
            <div>收藏</div>
          </el-col>
        </el-row>
        <el-divider />

        <el-row :gutter="10">


          <!-- <el-col class="comment1-box" v-for="comment in comments"> -->
          <el-col class="comment1-box">
            <div v-if="hover == false">
              <el-button type="primary" text bg @click="hover = true"> 评论</el-button>
            </div>
            <el-form :model="formdata" :rules="rules" v-else>
              <el-form-item label="">
                <el-input v-model="formdata.comment" placeholder="输入评论" />
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="onSubmit()">提交</el-button>
                <el-button type="primary" @click="hover = false">取消</el-button>
              </el-form-item>
            </el-form>
            <div class="comment1-box" v-for="comment in comments">
              <p>{{ comment.fromu }}&nbsp;&nbsp;{{ comment.date }}</p>
              <p>{{ comment.message }}</p>
            </div>
            <!-- <div class="comment2-box" v-for="comment2 in comment.comment2" :key="comment2.id" @mouseover="hover = true"
              @mouseleave="hover = false">
              <p class="user-comment2">{{ comment2.fromu }}&nbsp;回复&nbsp;{{ comment.fromu }}&nbsp;&nbsp;{{ comment.date
              }}</p> <span></span>
              <p>{{ comment2.message }}</p>
            </div> -->
          </el-col>
        </el-row>

      </el-card>
    </el-col>
    <el-col :span="12">
      <el-card class="article-card">
        <template #header>
          <div class="card-header">
            <div>{{ article.title }}</div>
            <div class="article-info">
              <span>于&nbsp;{{ article.create_date }} &nbsp;发布</span>
              <span @click="doUpvote()" style="cursor: pointer;text-decoration: underline;">{{ article.upvote }}
                &nbsp;赞</span>
              <span @click="doCollect()" style="cursor: pointer;text-decoration: underline;">{{ article.collect }}
                &nbsp;收藏</span>
              <span>{{ article.pageviews }} &nbsp;阅读量</span>
            </div>
          </div>
        </template>
        <div class="article-body">
          {{ article.body }}
        </div>


      </el-card>
    </el-col>
    <el-col :span="4">
    </el-col>
  </el-row>
</template>

<script setup lang="ts">
// 页面依赖
import { ref, onMounted, reactive, toRefs, } from 'vue';
import { ElMessage } from 'element-plus';

// 路由依赖
import { useRoute } from 'vue-router';
const route = useRoute();

// 状态管理依赖
import { useUserStore } from "@/store/modules/user";
const userStore = useUserStore();

// API 依赖
import { getArticleAPI, getCommentsApi, addComment1Api, addUpvoteCollectAPI } from "@/api/articles/index";
import { getUserInfo } from "@/api/user/index";

// 数据类型依赖
import { ArticleReadingType, Comment1Type } from "@/api/articles/types";
import { userCardType } from "@/api/user/types";
import { FormInstance, FormRules, messageConfig } from 'element-plus'


const hover = ref(false);

const rules = reactive<FormRules>({
  comment: { required: true, message: '不能为空', trigger: 'blur' },
});
const formdata = reactive({
  comment: '',
});


const state = reactive({
  article: {} as ArticleReadingType,
  author: {} as userCardType,
  comments: {} as Comment1Type,
});

const {
  article,
  author,
  comments,
} = toRefs(state);


async function onSubmit() {
  if (formdata.comment == '') {
    ElMessage.error('不能为空.');
  } else {
    await addComment1Api('v1', route.params.id, formdata)
      .then(() => {
        hover.value = false;
      })
      .catch(() => {
        ElMessage.warning('提交出错.');
      })
  }
};

function doUpvote() {
  addUpvoteCollectAPI('v1', '03010501', route.params.id)
    .then(() => {
      ElMessage.success('点赞成功');
      state.article.upvote += 1;
    })
}
function doCollect() {
  addUpvoteCollectAPI('v1', '03010502', route.params.id)
    .then(() => {
      ElMessage.success('收藏成功');
      state.article.collect += 1;
    })
}


function InitArticle() {
  getArticleAPI('v2', route.params.id)
    .then((data) => {
      console.log(data)
      state.article = data;
    })
};

function InitUserInfo() {
  getUserInfo('v2', '01040203', route.params.id)
    .then((data) => {
      state.author = data;
    })
};

function InitComment() {
  getCommentsApi('v1', route.params.id)
    .then((data) => {
      state.comments = data;
    })
};

function addPageviews() {
  addUpvoteCollectAPI('v1', '03010503', route.params.id)
    .then(() => {
      state.article.pageviews += 1;
    })
}
onMounted(() => {
  // 初始化 文章 详情
  InitArticle();
  // 初始化作者
  InitUserInfo();
  // 初始化评论
  InitComment();

  // 增加阅读量
  addPageviews
});

</script>

<style  lang="scss">
.user-card {
  .user-info {
    margin-bottom: 14px;
  }

  .user-item {
    text-align: center;
    margin-bottom: 14px;

  }
}

.article-card {
  .card-header {
    height: 50px;

    .article-info {
      display: flex;
      gap: 30px;
    }
  }

  .article-body {
    min-height: 1000px;
  }
}


//评论样式
.comment1-box {
  margin-bottom: 20px;

  .user {
    color: #3596eb;
  }

  .comment2-box {
    font-size: 1px;
    margin: 10px;

    .user-comment2 {
      color: #5eaaec;
    }

  }


}
</style>