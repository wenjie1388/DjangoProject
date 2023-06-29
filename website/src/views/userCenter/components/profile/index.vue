<template>
  <el-row>
    <el-col :span="24">
      <el-card body-style="display:flex">
        <el-avatar :size="150"
          src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
          class="avatar" />
        <div style="padding-left: 14px">
          <span>{{ userStore.nickname }}</span>
        </div>
      </el-card>
    </el-col>
  </el-row>

  <el-row style="padding-top:14px">
    <el-col :span="24">
      <el-card body-style="display:block;">
        <template #header>
          <div class="card-header">
            <span>基本信息</span>
          </div>
        </template>
        <el-form ref="ruleFormRef" :model="ruleForm" :rules="rules" label-width="120px" style="max-width: 460px"
          label-position="right">
          <el-form-item label="用户昵称">
            <el-input v-model="ruleForm.nickname" :disabled="isDisabled" />
          </el-form-item>
          <el-form-item label="用户id">
            <el-input v-model="ruleForm.id" :disabled="true" />
          </el-form-item>
          <el-form-item v-if="isDisabled">
            <el-button @click="isDisabled = false">编辑</el-button>
          </el-form-item>
          <el-form-item v-else>
            <el-button type="primary" @click="submitForm(ruleFormRef)">
              提交
            </el-button>
            <el-button @click="resetForm(ruleFormRef)">取消</el-button>
          </el-form-item>
        </el-form>
      </el-card>
    </el-col>
  </el-row>
</template>

<script setup lang="ts">
// 系统依赖
import { reactive, ref } from 'vue';

// Element 依赖
import type { FormInstance, FormRules } from 'element-plus';
import { ElMessage, ElMessageBox } from 'element-plus';


// 状态管理依赖
import { useUserStore } from "@/store/modules/user";
import { useAppStore } from "@/store/modules/app";
const userStore = useUserStore();

const ruleFormRef = ref<FormInstance>();

// 初始化禁用
const isDisabled = ref(true);

const ruleForm = reactive({
  nickname: userStore.nickname,
  id: userStore.id,
});

const rules = reactive<FormRules>({
  nickname: [
    { required: true, message: '账号不能空', trigger: 'change' },
    { min: 6, max: 24, message: '长度在6-24之间', trigger: 'change' },
  ]
});


const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return
  await formEl.validate((valid, fields) => {
    if (valid) {
      userStore.updateInfo(ruleForm)
        .then(() => {
          ruleForm.nickname = userStore.nickname;
          isDisabled.value = true;
        })
    } else {
      console.log('error submit!', fields);
    }
  });
};

const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  ruleForm.nickname = userStore.nickname;
  formEl.resetFields();
  isDisabled.value = true;
}


</script>

<style scoped></style>