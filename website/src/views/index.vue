<template>
  <el-row :gutter="0">
    <el-col :span="12" :offset="2">
      <div class="carousel-box grid-content" style="margin-left: 0px;">
        <el-carousel indicator-position="outside">
          <el-carousel-item v-for="item in 4" :key="item">
            <h3 text="2xl" justify="center">{{ item }}</h3>
          </el-carousel-item>
        </el-carousel>
      </div>
    </el-col>
    <el-col :span="6" style="margin-left: 20px;">
      <div class="grid-content hot-news">
        热点
      </div>
    </el-col>
  </el-row>

  <el-row :gutter="0">
    <el-col :span="12" :offset="2">
      <el-tabs v-model="activetabs" class="demo-tabs" @tab-click="handleClick">
        <el-tab-pane label="关注" name="Attention">

        </el-tab-pane>
        <el-tab-pane label="推荐" name="Recommend">
          <div class="card-box" v-for="info in data" style="display: flex;">
            <div class="left">
              <a :href="info.URL">
                <img :src="info.URL" alt="">
              </a>
            </div>
            <div class="right" style="width: auto; height: 100px;">
              <div class="title"><a href="#">{{ info.title }}</a></div>
              <div class="digest"><a href="">{{ info.digest }}</a></div>
              <div class="tags">
                <a href="#">{{ info.num }}颗<el-icon>
                    <Sugar />
                  </el-icon></a>
                <a href="#"></a>
                <a href="#">作者：{{ info.author }}</a>
              </div>
            </div>
          </div>
        </el-tab-pane>
        <el-tab-pane label="热榜" name="HotList">Role</el-tab-pane>
      </el-tabs>
    </el-col>
    <el-col :span="6" style="margin-left: 20px;">
      <!-- 预留位 -->
      <!-- <div class="grid-content hot-news"></div> -->
    </el-col>
  </el-row>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import type { TabsPaneContext, } from 'element-plus'
import { Sugar } from '@element-plus/icons-vue'
const activetabs = ref('Recommend')
const count = ref(0)
const load = () => {
  count.value += 2
}

const data = [
  {
    URL: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
    title: '【云原生 | 51】Docker三剑客之Docker Compose第二节',
    digest: '对于Compose来说，大部分命令的对象既可以是项目本身，也可以指定为项目中的服务或者容器。如果没有特别说明，命令对象将是项目，这意味着项目中所有的服务都会受到命令影响。',
    num: '12',
    author: '小鹏linux',
  },
  {
    URL: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
    title: '算法leetcode｜25. K 个一组翻转链表（rust重拳出击）',
    digest: '给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。',
    num: '23',
    author: '二当家的白帽子',
  },
  {
    URL: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
    title: '【最优潮流】直流最优潮流(OPF)课设（Matlab代码实现）',
    digest: '最优潮流(OPF)是指在满足电网约束的同时，以最小的成本将负荷分配给电厂。描述为在满足网络(潮流)约束的情况下最小化所有承诺的工厂的总燃料成本的优化问题。',
    num: '0',
    author: '@橘柑橙柠桔柚',
  },
  {
    URL: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
    title: '很喜欢这个数字',
    digest: '对于Compose来说，大部分命令的对象既可以是项目本身，也可以指定为项目中的服务或者容器。如果没有特别说明，命令对象将是项目，这意味着项目中所有的服务都会受到命令影响。',
    num: '10',
    author: '认真学习的小雅兰.',
  },
]

const handleClick = (tab: TabsPaneContext, event: Event) => {
  console.log(tab, event)
}
</script>

<style lang="scss">
.el-col {
  border-radius: 4px;
}

.grid-content {
  background-color: brown;
}

.card-box {
  /* border: solid 1px #e0e0e0; */
  border-top: solid 1px #e0e0e0;
  border-bottom: solid 1px #e0e0e0;
  margin-bottom: 18px;

  .left {
    display: flex;
    margin-right: 16px;
    padding-top: 2px;

    img {
      width: 178px;
      height: 100px;
    }
  }

  .right {
    .tags {
      display: flex;
      flex-direction: row;
    }

    a {
      color: black;
    }
  }
}
</style>
