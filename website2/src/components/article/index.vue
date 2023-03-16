<template>
  <el-space direction="vertical" :fill="true">
    <el-card v-for="i in 2" :key="i" class="box-card" style="width: 31vw">
      <template #header>
        <div class="card-header">
          <span>标题标题标题标题标题标题标题标</span>
          <el-button class="button" text disabled>详情</el-button>
        </div>
      </template>
      <el-space direction="horizontal">
        <el-image style="width: 100px; height: 100px"
          src="'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg'" fit="scale-down" />
        <el-space direction="vertical" :fill="true" :size="0" style="height: 100px ;" space-items='t'>
          <div class="article-digest-container">
            <span>
              摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要摘要
            </span>
          </div>
          <div class="article-tag-container">
            <span> 文章标签1 </span>|<span> 文章标签2 </span>
          </div>
        </el-space>

      </el-space>
    </el-card>
  </el-space>
</template>

<script setup lang="ts">


</script>

<style scoped>
.article-digest-container {
  color: black;
  font-size: 13px;
  height: 75px;
  /* 超高显示省略号 */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 4;
  overflow: hidden;
}

.article-tag-container {
  font-size: 1px;
  color: #6c6c6ccf;
}
</style>