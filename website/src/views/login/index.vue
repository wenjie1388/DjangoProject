<template>
  <el-row :gutter="20">
    <el-col :span="5">
      <div class="grid-content ep-bg-purple" />
    </el-col>
    <el-col :span="5">
      <div class="grid-content ep-bg-purple" />
    </el-col>
    <el-col :span="5">
      <el-tabs type="border-card">
        <el-tab-pane label="登录">
          <el-form ref="loginRef" :model="loginData" status-icon :rules="loginRules" label-width="80px"
            :hide-required-asterisk="isasterisk">
            <el-form-item label="账号：" prop="username">
              <el-input v-model="loginData.username" type="input" placeholder="用户名/邮箱/手机号码" />
            </el-form-item>
            <el-form-item label="密码：" prop="password">
              <el-input v-model="loginData.password" type="password" autocomplete="off" show-password
                placeholder="8-24，数字、字母与符号_,.!#~?&^" maxlength="24" />
            </el-form-item>
            <el-form-item label="验证码：" prop="captcha">
              <el-input v-model="loginData.captcha" type="input" autocomplete="off" maxlength="6" size="" width="50px"
                class="inputCode-con" placeholder="******" />
              <el-button @click="sendCode(loginRef)" :disabled="isdisabled">
                <span v-if="!isdisabled">发送验证码</span>
                <span v-else>{{ time60s }} 秒后重试</span>
              </el-button>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="submitForm(loginRef)" :isdisabled="isdisabled">登录</el-button>
              <el-button type="primary" @click="registerForm(loginRef)">注册</el-button>
            </el-form-item>
          </el-form>
        </el-tab-pane>
      </el-tabs>
    </el-col>
    <el-col :span="5">
      <div class="grid-content ep-bg-purple" />
    </el-col>
    <el-col :span="5">
      <div class="grid-content ep-bg-purple" />
    </el-col>
  </el-row>
</template>

<script setup lang="ts">
// 页面依赖
import { reactive, ref, toRefs } from 'vue';
import type { FormInstance, FormRules } from 'element-plus'
import router from "@/router";
import { ElMessage } from 'element-plus';

// 状态管理依赖
import { useUserStore } from "@/store/modules/user";
const userStore = useUserStore();

// API依赖
import { LocationQuery, LocationQueryValue, useRoute } from "vue-router";
import { getCaptchaApi } from "@/api/auth";
import { LoginDataC, Captcha } from "@/api/auth/types";

// 倒计时时长
const time60s = ref(60);

/**
 * 按钮loading
 */
const loading = ref(false);

/**
 * 是否大写锁定
 */
const isCapslock = ref(false);

/**
 * 密码是否可见
 */
const passwordVisible = ref(false);
/**
 * 按钮是否禁用
 */
const isdisabled = ref(false);
/**
 * 是否隐藏*号标记
 */
const isasterisk = ref(true);

const route = useRoute();
const loginRef = ref<FormInstance>();
const loginData = ref<LoginDataC>({
  username: "",
  password: "",
  captcha: ""
});
const loginRules = reactive<FormRules>({
  username: [
    { required: true, message: '账号不能空', trigger: 'change' },
    { min: 6, max: 24, message: '长度在6-24之间', trigger: 'change' },
  ],
  password: [
    { required: true, message: '密码不能空', trigger: 'change' },
    { min: 8, max: 24, message: '长度在8-24之间', trigger: 'change' },
  ],
  captcha: [
    { required: true, message: '验证码不能空', trigger: 'change' },
    { min: 6, max: 6, message: '长度为6', trigger: 'change' },
  ],
});



const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return
  await formEl.validate((valid, fields) => {
    if (valid) {
      loading.value = true;
      userStore
        .login(loginData.value)
        .then(() => {
          router.push('/');
        })
        .catch(() => {
          ElMessage({
            message: '用户名或密码错误',
            type: 'warning'
          });
        })
        .finally(() => {
          loading.value = false;
        })
    } else {
      isasterisk.value = false
      ElMessage({
        message: '填写不完整',
        type: 'warning',
      })
    }
  })
};

const registerForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.resetFields()
};

const sendCode = async (formEl: FormInstance | undefined) => {
  if (formEl?.validateField(["username", "password"])) {
    // 倒计时
    const timer = await setInterval(() => {
      isdisabled.value = true;
      time60s.value -= 1;
      if (time60s.value == 0) {
        isdisabled.value = false;
        time60s.value = 60;
        clearTimeout(timer);
      };
    }, 1000);
    const captcha = await getCaptchaApi(loginData.value.username)
      .then((data) => {
        const { captcha } = data;
        console.log(captcha, data);
      });
  };
};

</script>

<style scoped lang="scss">
.inputCode-con {
  width: 80px;
  margin-right: 20px;
}
</style>