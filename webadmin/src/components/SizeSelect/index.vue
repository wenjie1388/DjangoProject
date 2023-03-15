<script setup lang="ts">
import { ref } from 'vue';
import { ElMessage } from 'element-plus';

import { useAppStore } from '@/store/modules/app';
import SvgIcon from '@/components/SvgIcon/index.vue';

const appStore = useAppStore();

const sizeOptions = ref([
  { label: '默认', value: 'default' },
  { label: '大型', value: 'large' },
  { label: '小型', value: 'small' }
]);

function handleSizeChange(size: string) {
  appStore.changeSize(size);
  ElMessage.success('切换布局大小成功');
}
</script>

<template>
  <el-dropdown trigger="click" @command="handleSizeChange">
    <div class="cursor-pointerw-[40px] h-[50px] leading-[50px] text-center">
      <svg-icon icon-class="size" />
    </div>
    <template #dropdown>
      <el-dropdown-menu>
        <el-dropdown-item v-for="item of sizeOptions" :key="item.value" :disabled="appStore.size == item.value"
          :command="item.value">
          {{ item.label }}
        </el-dropdown-item>
      </el-dropdown-menu>
    </template>
  </el-dropdown>
</template>


<style>
.navbar .navbar-right .navbar-setting-wrapper .navbar-setting-item {
  height: 50px;
  line-height: 50px;
  padding: 0 8px;
  display: inline-block;
  cursor: pointer;
  color: #5a5e66;
}

.el-dropdown {
  --el-dropdown-menu-box-shadow: var(--el-box-shadow-light);
  --el-dropdown-menuItem-hover-fill: var(--el-color-primary-light-9);
  --el-dropdown-menuItem-hover-color: var(--el-color-primary);
  --el-dropdown-menu-index: 10;
  display: inline-flex;
  position: relative;
  color: var(--el-text-color-regular);
  font-size: var(--el-font-size-base);
  line-height: 1;
  vertical-align: top;
}

.svg-icon {
  display: inline-block;
  outline: none;
  width: 1em;
  height: 1em;
  vertical-align: -0.15em;
  fill: currentColor;
  overflow: hidden;
}
</style>