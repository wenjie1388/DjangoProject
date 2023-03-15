<template>
  <el-form ref="loginRef" :model="loginForm" status-icon :rules="loginRules" label-width="120px" class="demo-ruleForm">
    <el-form-item label="账号" prop="username">
      <el-input v-model="loginForm.username" type="input" placeholder="请输入用户名" clearable>
      </el-input>
    </el-form-item>
    <el-form-item label="密码" prop="password">
      <el-input v-model="loginForm.password" type="password" placeholder="请输入密码" show-password>
      </el-input>
    </el-form-item>
    <el-form-item>
      <!-- <el-button type="primary" @click="submitForm(loginRef)">登录</el-button> -->
      <el-button type="primary">登录</el-button>

    </el-form-item>
  </el-form>
</template>

<script setup lang="ts">
import { FormInstance } from 'element-plus/es/components/form';
import { reactive, ref } from 'vue';
// import { login } from '../../api/user';
import { useRouter } from "vue-router";
// import Cookies from 'js-cookie'


const router = useRouter();
const loginRef = ref<FormInstance>();

// 登录表单数据
const loginForm = reactive({
  username: "wenjie12",
  password: "a1234567",
  // code: '123456',
});
// 登录规则校验
const loginRules = reactive({
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' },
    { min: 5, max: 16, message: " 5 - 16 个字符", trigger: "blur" }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 6, max: 20, message: " 6 - 20 个字符", trigger: "blur" }
  ],
  // code: [
  //   { required: true, message: '请输入验证码', trigger: 'blur' },
  //   { min: 6, max: 6, message: " 6 个字符", trigger: "blur" }
  // ],
})

const test = () => {
  console.log(document.cookie);
}
/**
// 登录表单逻辑
const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.validate(async (valid) => {
    if (valid) {
      // let res = await $login('user/login', loginForm)
      let { data, status, statusText } = await $login('user/login', loginForm)
      // console.log(res);
      // 获取
      // console.log(data, status, statusText);
      switch (status) {
        case 200: {
          // 登录成功 200
          localStorage.setItem("username", data['username'])
          $mes_success('登录成功，欢迎回来 ' + data['username'] + ' ^.^')
          router.go(0)
          router.push({
            path: '/',
            // params: {
            //   username: localStorage.getItem('username')
            // }
          })

        }
          break
        case 404: {
          // 登录失败 404
          console.log('登录404')
        }

      }
    }
  })
} */
</script>

<style scoped></style>