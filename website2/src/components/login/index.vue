<template>
  <el-card shadow="hover" v-if="loading">
    <!-- 头像 -->
    <div class=" item">
      <el-avatar :size="50" src="https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png" />
    </div>
    <!-- 名字 -->
    <div class="item">
      <!-- <span>{{ userStore.name }}</span> -->
      <span> <a href="/admin">wenjie</a></span>

    </div>
    <div class="item">
      <span>点赞量|阅读量|访问量</span>
    </div>
  </el-card>
  <el-card shadow="never" v-else>
    <el-form ref="ruleFormRef" :model="loginfrom" status-icon :rules="rules" label-width="4vw" class="loginfrom"
      label-position="left">
      <el-form-item label="用户名：" prop="username">
        <el-input v-model="loginfrom.username" type="input" autocomplete="off" />
      </el-form-item>
      <el-form-item label="密码：" prop="password">
        <el-input v-model="loginfrom.password" type="password" autocomplete="off" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm(ruleFormRef)">登录</el-button>
        <!-- <el-button @click="resetForm(ruleFormRef)">Reset</el-button> -->
      </el-form-item>
    </el-form>
  </el-card>
</template>

<script lang="ts" setup>
import { reactive, ref, onMounted } from 'vue';
import type { FormInstance } from 'element-plus';
import { loginApi } from '../../api/auth/index'
import { useUserStore } from '../../store/modules/user'
import router from '../../router';

const userStore = useUserStore();
const loading = ref(true)

const ruleFormRef = ref<FormInstance>()

const validateusername = (rule: any, value: any, callback: any) => {
  if (value === '') {
    callback(new Error('Please input the password'))
  } else {
    if (loginfrom.username !== '') {
      if (!ruleFormRef.value) return
      ruleFormRef.value.validateField('checkPass', () => null)
    }
    callback()
  }
}
const validatepassword = (rule: any, value: any, callback: any) => {
  if (value === '') {
    callback(new Error('请输入密码'))
  } else {
    if (loginfrom.password !== '') {
      if (!ruleFormRef.value) return
      ruleFormRef.value.validateField('checkPass', () => null)
    }
    callback()
  }
}
const loginfrom = reactive({
  username: '',
  password: '',
})

const rules = reactive({
  username: [{ validator: validateusername, trigger: 'blur' }],
  password: [{ validator: validatepassword, trigger: 'blur' }],
})

const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.validate((valid) => {
    if (valid) {
      console.log('submit!')
    } else {
      console.log('error submit!')
      return false
    }
  })
}

// const resetForm = (formEl: FormInstance | undefined) => {
//   if (!formEl) return
//   formEl.resetFields()
// }

const state = reactive({
  loginData: {
    'username': 'wenjie1',
    'password': 'wenjie1'
  }
})

function getUser() {
  // loginApi(state.loginData)
  //   // let jackson = aw loginApi(state.loginData) => { }
  //   .then((res) => {
  //     const { msg, code, username } = res.data
  //     console.log(msg, code, username, res.data)
  //     loading.value = true
  //     router.push('/')
  //   })
  userStore.login(state.loginData)
  loading.value = true
  console.log(loading.value)
}

onMounted(() => {
  getUser();
})

</script>

<style scoped>
.loginfrom {
  padding: 0;
  margin: 0 auto;
  text-align: center;
}

.item {
  padding: 0;
  margin: 0 auto;
  text-align: center;
}
</style>