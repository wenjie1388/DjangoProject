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
        <el-tab-pane label="注册">
          <el-form ref="loginRef" :model="registerData" status-icon :rules="loginRules" label-width="100px"
            :hide-required-asterisk="isasterisk">
            <el-form-item label="账号：" prop="username">
              <el-input v-model="registerData.username" type="input" placeholder="邮箱/手机号码" />
            </el-form-item>
            <el-form-item label="密码：" prop="password">
              <el-input v-model="registerData.password" type="password" autocomplete="off" show-password
                placeholder="8-24，数字、字母与符号_,.!#~?&^" maxlength="24" />
            </el-form-item>
            <el-form-item label="重复密码：" prop="checkPass">
              <el-input v-model="registerData.checkPass" type="password" autocomplete="off" show-password
                placeholder="再次输入" maxlength="24" />
            </el-form-item>
            <el-form-item label="验证码：" prop="captcha">
              <el-input v-model="registerData.captcha" type="input" autocomplete="off" maxlength="6" size="" width="50px"
                class="inputCode-con" placeholder="******" />
              <el-button @click="sendCode(loginRef)" :disabled="isdisabled">
                <span v-if="!isdisabled">发送验证码</span>
                <span v-else>{{ time60s }} 秒后重试</span>
              </el-button>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="registerForm(loginRef)" :isdisabled="isdisabled">注册</el-button>
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

// 数据类型依赖
import { registerDataC } from "@/api/auth/types";

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
const registerData = reactive<registerDataC>({
  username: "",
  password: "",
  checkPass: "",
  captcha: "",
});

const validatePass = (rule: any, value: any, callback: any) => {
  if (value === '') {
    callback(new Error('Please input the password again'))
  } else if (value !== registerData.password) {
    callback(new Error("两次输入的的密码不一致!"))
  } else {
    callback()
  }
}
const loginRules = reactive<FormRules>({
  username: [
    { required: true, message: '账号不能空', trigger: 'change' },
    { min: 6, max: 24, message: '长度在6-24之间', trigger: 'change' },
  ],
  password: [
    { required: true, message: '密码不能空', trigger: 'change' },
    { min: 8, max: 24, message: '长度在8-24之间', trigger: 'change' },
  ],
  checkPass: [{ validator: validatePass, trigger: 'blur' }],
  captcha: [
    { required: true, message: '验证码不能空', trigger: 'change' },
    { min: 6, max: 6, message: '长度为6', trigger: 'change' },
  ],
});



const registerForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return
  await formEl.validate((valid, fields) => {
    if (valid) {
      loading.value = true;
      userStore
        .login(registerData)
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
    const captcha = await getCaptchaApi(registerData.username)
      .then((data) => {
        console.log(data);
      });
  };
};

</script>

<style scoped></style>