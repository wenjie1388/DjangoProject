<template>
  <el-row :gutter="0">
    <el-col :span="7" :offset="12">
      <el-tabs tab-position="left" v-model="activeName" style="height: 200px" class="demo-tabs">
        <el-tab-pane label="微信登录" name="first">微信登录</el-tab-pane>
        <el-tab-pane label="免密登录" name="second">免密</el-tab-pane>
        <el-tab-pane label="密码登录" name="third">
          <AccountVue />
        </el-tab-pane>
        <el-tab-pane label="其它登录" name="fourth">其它</el-tab-pane>
      </el-tabs>
    </el-col>
  </el-row>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import AccountVue from '../../components/login/account.vue'

const activeName = ref('first')


</script>
<style>
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
  background-color: aquamarine;
}
</style>
