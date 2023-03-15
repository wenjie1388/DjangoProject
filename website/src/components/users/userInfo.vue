<template>
  <el-row :gutter="10">
    <el-col :span="4" :offset="5">
      <div class="grid-content">
        <el-avatar :size="200" shape="circle" src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png" />
      </div>
    </el-col>
    <el-col :span="12" :offset="0">
      <div class="grid-content" style="height: 9vw;">
        个性签名
      </div>
      <div class="grid-content">
        其余链接和标签
      </div>
    </el-col>

  </el-row>


  <el-row :gutter="10">
    <el-col :span="12" :offset="5">
      <div class="grid-content">
        <el-form label-position="right" label-width="100px" :model="formInfo" style="max-width: 460px">
          <el-form-item :label="info.lable" v-for="info in userInfo">
            <el-input v-model="info.fileName" :value="info.value" :disabled="isDisabled"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button @click="isDisabled = false" v-if="isDisabled">编辑</el-button>
            <div v-else>
              <el-button type="primary" @click="submitForm(formRef)">提交</el-button>
              <el-button @click="isDisabled = true">取消</el-button>
            </div>
          </el-form-item>
        </el-form>
      </div>
    </el-col>

  </el-row>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'
import type { FormInstance } from 'element-plus'

const formRef = ref<FormInstance>()
const isDisabled = ref(true)
const userInfo = [
  { fileName: 'username', lable: "用户昵称", value: "JayeJOJO" },
  { fileName: 'id', lable: "用户ID", value: "qq_41935112" },
  { fileName: 'gender', lable: "性别", value: "男" },
  { fileName: 'birthdate', lable: "出生日期", value: "1997 - 10 - 07" },
  { fileName: 'individual', lable: "个人简介", value: "未填写" },
  { fileName: 'userUS', lable: "所在地区", value: "" },
]

const formInfo = reactive({
  username: '',
  id: '',
  gender: '',
  birthdate: '',
  individual: '',
  userUS: '',
})



const submitForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.validate((valid) => {
    if (valid) {
      console.log('submit!')
      console.log(formInfo)

    } else {
      console.log('error submit!')
      return false
    }
  })
}

</script>

<style scoped>
.el-row {
  margin-bottom: 20px;
}

.el-row:last-child {
  margin-bottom: 0;
}

.el-col {
  border-radius: 5px;
  padding-right: 0px;
  padding-left: 0px;
  margin-left: 0px;
}

.el-col-4 {
  flex: 0
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
</style>