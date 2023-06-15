<template>
  <el-row>
    <el-col :span="24">
      <el-card class="box-card">
        <template #header>
          <div class="card-header">
            <span>基本信息</span>
          </div>
        </template>
        <el-form ref="ruleFormRef" :model="ruleForm" :rules="rules" label-width="120px" style="max-width: 460px"
          label-position="right">
          <el-form-item label="密码">
            <el-input v-model="ruleForm.password" :disabled="isDisabled" type="password" />
          </el-form-item>
          <el-form-item label="手机">
            <el-input v-model="ruleForm.cellphone" :disabled="isDisabled" />
          </el-form-item>
          <el-form-item label="邮箱">
            <el-input v-model="ruleForm.email" :disabled="isDisabled" />
          </el-form-item>
          <el-form-item v-if="isDisabled">
            <el-button @click="isDisabled = false">编辑</el-button>
          </el-form-item>
          <el-form-item v-else>
            <el-button type="primary"
              @click="verifyOne(ruleFormRef, ruleForm.password, ruleForm.cellphone, ruleForm.email)">
              提交
            </el-button>
            <el-dialog v-model="centerDialogVisible" title="Warning" width="30%" align-center
              :close-on-click-modal="false">
              <div v-if="ruleForm.email">已向{{ ruleForm.email }}发送验证码：</div>
              <div v-else>已向{{ ruleForm.cellphone }}发送验证码：</div>
              <el-form-item label="验证码">
                <el-input v-model="ruleForm.captcha" :disabled="isDisabled" />
              </el-form-item>
              <template #header>
                <span>验证码校验</span>
              </template>
              <template #footer>
                <span class="dialog-footer">
                  <el-button @click="centerDialogVisible = false">取消</el-button>
                  <el-button type="primary" @click="submitForm(ruleFormRef)">
                    提交
                  </el-button>
                </span>
              </template>
            </el-dialog>
            <el-button @click="resetForm(ruleFormRef)">取消</el-button>
          </el-form-item>
        </el-form>
      </el-card>
    </el-col>
  </el-row>
</template>

<script setup lang="ts">
// 系统依赖
import { reactive, ref, onMounted } from 'vue';
import type { FormInstance, FormRules } from 'element-plus';

// Element 依赖
import { ElMessage, ElMessageBox } from 'element-plus';

// 路由依赖
import router from '@/router';

// 状态管理依赖
import { useUserStore } from "@/store/modules/user";
import { useAppStore } from "@/store/modules/app";
const userStore = useUserStore();
const ruleFormRef = ref<FormInstance>();

/**
 * 数据类型依赖管理
 */
import { captchaEmailInfo, captchaPhoneInfo } from "@/api/auth/types";

// 初始化禁用
const isDisabled = ref(true);
// 初始化对话框
const centerDialogVisible = ref(false);

const ruleForm = reactive({
  id: userStore.id,
  password: userStore.password,
  cellphone: userStore.cellphone,
  email: userStore.email,
  captcha: userStore.captcha,
});

const rules = reactive<FormRules>({
  password: [
    { required: true, message: '密码不能空', trigger: 'change' },
    { min: 8, max: 24, message: '长度在8-24之间', trigger: 'change' },
  ],
  cellphone: [
    { required: true, message: '手机号不能空', trigger: 'change' },
    { min: 11, max: 11, message: '长度是11', trigger: 'change' },
  ],
  email: [
    { required: true, message: '邮箱不能空', trigger: 'change' },
  ]
});


/**
 * 第一次提交
 * @param formEl 表单验证
 * @param pw 密码
 * @param phone 手机号
 * @param em 邮箱
 */
function verifyOne(formEl: FormInstance | undefined, pw: string, phone: string, em: string) {
  if (!formEl) return
  if ((pw === userStore.password) && (em === userStore.email) && (phone === userStore.cellphone)) {
    ElMessage({
      message: '未有修改',
      type: 'warning',
    });
  } else {
    var captchaInfo = '';
    if (em) {
      captchaInfo = phone;
    } else {
      captchaInfo = em;
    }
    centerDialogVisible.value = true;
    userStore.getCaptcha(captchaInfo)
      .then(() => {
        console.log(userStore.captcha)
      })
  };
};


/**
 * 第二次提交
 * @param formEl 表单验证
 */
const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return
  await formEl.validate((valid, fields) => {
    if (valid) {
      isDisabled.value = true;
      if (ruleForm.captcha === userStore.captcha) {
        userStore.updateAccountInfo(ruleForm)
          .then(() => {
            ElMessage({
              message: '修改成功',
              type: 'success',
            });
            userStore.resetCaptcha();
            router.go(0);
          });
      } else {
        ElMessage.error('验证码错误');
      }
    } else {
      console.log('error submit!', fields);
    }
  })
};


const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  isDisabled.value = true;
  formEl.resetFields();
};


// 初始化账号信息
function initAccountInfo() {
  userStore.getAccountInfo()
    .then(() => {
      ruleForm.password = userStore.password;
      ruleForm.cellphone = userStore.cellphone;
      ruleForm.email = userStore.email;
    })
};

onMounted(() => {
  // 初始化用户账号信息
  initAccountInfo();
});

function sendCode() {
  throw new Error('Function not implemented.');
}
</script>

<style scoped></style>