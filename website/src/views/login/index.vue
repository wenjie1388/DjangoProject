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
          <el-form ref="loginRef" :model="loginForm" status-icon :rules="loginRules" label-width="80px"
            hide-required-asterisk="True">
            <el-form-item label="账号：" prop="username">
              <el-input v-model="loginForm.username" type="input" placeholder="用户名/邮箱/手机号码" />
            </el-form-item>
            <el-form-item label="密码：" prop="password">
              <el-input v-model="loginForm.password" type="password" autocomplete="off" show-password
                placeholder="8-24，数字、字母与符号_,.!#~?&^" maxlength="24" />
            </el-form-item>
            <el-form-item label="验证码：" prop="code">
              <el-input v-model="loginForm.code" type="input" autocomplete="off" maxlength="6" size="" width="50px"
                class="inputCode-con" placeholder="******" />
              <el-button @click="sendCode(loginRef)">发送验证码</el-button>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="submitForm(loginRef)">登录</el-button>
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
import { reactive, ref } from 'vue';
import type { FormInstance, FormRules } from 'element-plus';

const loginRef = ref<FormInstance>()
const loginForm = reactive({
  username: "",
  password: "",
  code: ""
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
  code: [
    { required: true, message: '验证码不能空', trigger: 'change' },
    { min: 6, max: 6, message: '长度为6', trigger: 'change' },
  ],
});

const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return
  await formEl.validate((valid, fields) => {
    if (valid) {
      console.log('submit!')
    } else {
      console.log('error submit!', fields)
    }
  })
};

const registerForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.resetFields()
};

const sendCode = async (formEl: FormInstance | undefined) => {
  // if (formEl?.validateField(["username", "password"])) {
  //   console.log(loginForm.password)
  // }

  // await formEl?.validate((valid, fields) => {
  //   if (valid) {
  //     console.log(valid, fields)
  //   } else {
  //     console.log('error submit!', fields)
  //   }
  // });
};


</script>

<style scoped lang="scss">
.inputCode-con {
  width: 80px;
  margin-right: 20px;
}
</style>