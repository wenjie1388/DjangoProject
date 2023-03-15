<script lang="ts">
export default {
  name: 'user'
};
</script>

<script setup lang="ts">
import {
  reactive,
  ref,
  watchEffect,
  onMounted,
  getCurrentInstance,
  toRefs
} from 'vue';

// api
import {
  QueryUserList, // 查询
  getUserForm,
  deleteUsers,
  addUser,
  updateUser,
  updateUserStatus,
  updateUserPassword,
  downloadTemplate,
  exportUser,
  importUser
} from '@/api/user';

import { getSmsCaptcha } from '@/api/auth';
import { ElTree, ElForm, ElMessageBox, ElMessage, UploadFile } from 'element-plus';
import {
  Search,
  Plus,
  Refresh,
  Delete,
} from '@element-plus/icons-vue';
import {
  UserAddForm,
  UserImportData,
  UserQuery,
  UserListType,
  UserPages
} from '@/api/user/types';
import { stringifyExpression } from '@vue/compiler-core';
import { rest } from 'lodash';
import { fa } from 'element-plus/es/locale';

const queryFormRef = ref(ElForm); // 查询表单
const dataFormRef = ref(ElForm); // 用户表单

const { proxy }: any = getCurrentInstance();

const state = reactive({
  loading: true,  // 遮罩层
  ids: [] as number[],  // 选中数组
  total: 0,   // 总条数
  time: 60,   // 倒计时
  captcha: '',
  userList: [] as UserListType[],
  dialog: {
    visible: false
  } as DialogType,
  userAddFormData: {
    status: 1
  } as UserAddForm,
  queryParams: {} as UserQuery,
  PagesParams: {
    pageNum: 1,
    pageSize: 10
  } as UserPages,
  rules: {
    username: [{
      pattern: /^[a-zA-Z\u4e00-\u9fa5](?![0-9]+$)(?![a-zA-Z]+$)([a-z-A-Z0-9\u4e00-\u9fa5]{5,19}$)/,
      required: true, message: '不为空,字母或汉字开头,6-20字符,字母、汉字、数字,不能全字母和数字', trigger: 'blur',
    }],
    password: [{
      pattern: /^[a-zA-Z](?![0-9]+$)(?![a-zA-Z]+$)(?![a-zA-Z0-9]+$)([a-z-A-Z0-9@,.!#~?&^]{5,23}$)/,
      required: true, message: '不为空,字母或开头,6-24字符,必须是字母、数字、@,.!#~?&^三种类型', trigger: 'blur',
    }],
    cell: [{
      pattern: /^1[3|4|5|6|7|8|9][0-9]\d{8}$/,
      required: true, message: '手记号码不能为空', trigger: 'blur',
    }],
    code: [{
      pattern: /^(?![0-9]+$)(?![a-zA-Z]+$)([a-z-A-Z0-9]{6}$)/,
      message: '验证码不能为空', trigger: 'blur',
    }],
    email: [
      {
        pattern: /\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}/,
        message: '请输入正确的邮箱地址',
        trigger: 'blur',
      }
    ],
  },
});

const { loading, ids, total, userList, dialog, userAddFormData, queryParams, PagesParams, rules, time } = toRefs(state);

/**
 * 初始化用户列表 And 查询用户列表
 */
function handleQuery() {
  state.loading = true;
  QueryUserList(state.queryParams).then(({ data }) => {
    state.userList = data.list;
    state.total = data.total;
    state.loading = false;
  });
}


/**
 * 获取验证码
 */
async function handleSmsCode() {
  state.loading = true;
  dataFormRef.value.validate((valid: any) => {
    if (valid) {
      getSmsCaptcha(userAddFormData.value.cell)
        .then(({ data }) => {
          state.captcha = data.SMScode;
          console.log(state.captcha);
        });
      var countDown = setInterval(async () => {
        state.time--;
        if (state.time == 0) {
          state.time = 30;
          state.loading = false;
          clearInterval(countDown);
        };
      }, 1000);
      state.loading = false;
    }
    else {
      state.loading = false;
    };
  });
}


/**
 * 重置
 */
function resetQuery() {
  queryFormRef.value.resetFields();
  handleQuery();
}


/**
 * 用户状态change
 */
function handleStatusChange(row: { [key: string]: any }) {
  const text = row.status === 1 ? '启用' : '停用';
  ElMessageBox.confirm(
    '确认要' + text + '' + row.username + '用户吗?',
    '警告',
    {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    }
  )
    .then(() => {
      return updateUserStatus(row.id, row.status);
    })
    .then(() => {
      ElMessage.success(text + '成功');
    })
    .catch(() => {
      row.status = row.status === 1 ? 0 : 1;
    });
}

/**
 * 行选中
 */
function handleSelectionChange(selection: any) {
  state.ids = selection.map((item: any) => item.id);
}

/**
 * 重置密码
 */
function resetPassword(row: { [key: string]: any }) {
  ElMessageBox.prompt(
    '请输入用户「' + row.username + '」的新密码',
    '重置密码',
    {
      confirmButtonText: '确定',
      cancelButtonText: '取消'
    }
  )
    .then(({ value }) => {
      if (!value) {
        ElMessage.warning('请输入新密码');
        return false;
      }
      updateUserPassword(row.id, value).then(() => {
        ElMessage.success('密码重置成功，新密码是：' + value);
      });
    })
    .catch(() => { });
}

/**
 * 添加用户
 **/
async function handleAdd() {
  state.dialog = {
    title: '添加用户',
    visible: true
  };
}

/**
 * 修改用户
 **/
async function handleUpdate(row: { [key: string]: any }) {
  dialog.value = {
    title: '修改用户',
    visible: true
  };

  const userId = row.id || state.ids;
  // await getDeptOptions();
  // await getRoleOptions();
  getUserForm(userId).then(({ data }) => {
    // userAddFormData.value = data;
  });
}

/**
 * 表单提交
 */
function submitForm() {
  state.loading = true;
  if (state.captcha == userAddFormData.value.code) {
    dataFormRef.value.validate((valid: any) => {
      if (valid) {
        addUser
      } else {
        state.loading = false;
      }
    });
  } else {
    ElMessage.error('验证码错误');
    state.loading = false;
  }
  // dataFormRef.value.validate((valid: any) => {
  //   if (valid) {
  // const userId = state.userAddFormData.id;
  // if (userId) {
  // updateUser(userId, state.userAddFormData).then(() => {
  //   ElMessage.success('修改用户成功');
  //   closeDialog();
  //   handleQuery();
  // });
  // } else {
  //   addUser(state.userAddFormData).then(() => {
  //     ElMessage.success('新增用户成功');
  //     closeDialog();
  //     handleQuery();
  //   });
  // }
  // }
  // });
}

/**
 * 删除用户
 */
function handleDelete(row: { [key: string]: any }) {
  const userIds = row.id || state.ids.join(',');
  ElMessageBox.confirm(
    '是否确认删除用户编号为「' + userIds + '」的数据项?',
    '警告',
    {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    }
  )
    .then(function () {
      deleteUsers(userIds).then(() => {
        ElMessage.success('删除成功');
        handleQuery();
      });
    })
    .catch(() => ElMessage.info('已取消删除'));
}

/**
 * 关闭用户弹窗
 */
function closeDialog() {
  dialog.value.visible = false;
  state.loading = false;
  dataFormRef.value.resetFields();
  dataFormRef.value.clearValidate();
  // userAddFormData.value.id = undefined;
}


/**
 * 导出用户
 */
function handleExport() {
  exportUser(queryParams.value).then((response: any) => {
    const blob = new Blob([response.data], {
      type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;charset=utf-8'
    });
    const a = document.createElement('a');
    const href = window.URL.createObjectURL(blob); // 下载的链接
    a.href = href;
    a.download = decodeURI(
      response.headers['content-disposition'].split(';')[1].split('=')[1]
    ); // 获取后台设置的文件名称
    document.body.appendChild(a);
    a.click(); // 点击导出
    document.body.removeChild(a); // 下载完成移除元素
    window.URL.revokeObjectURL(href); // 释放掉blob对象
  });
}

onMounted(() => {
  // 初始化性别字典
  // getGenderOptions();
  // 初始化部门
  // getDeptOptions();
  // 初始化用户列表数据
  handleQuery();
});
</script>

<template>
  <div class="app-container">
    <el-row :gutter="20">
      <!-- 用户数据 -->
      <el-col :span="20" :xs="24">
        <div class="search">
          <el-form ref="queryFormRef" :model="queryParams" :inline="true">
            <el-form-item label="关键字" prop="keywords">
              <el-input v-model="queryParams.username" placeholder="用户名" clearable style="width: 200px"
                @keyup.enter="handleQuery" />
            </el-form-item>

            <!-- <el-form-item label="是否激活" prop="status">
                                                                                                                                                                                      <el-select v-model="queryParams.active" placeholder="全部" clearable style="width: 200px">
                                                                                                                                                                                        <el-option label="激活" value="1" />
                                                                                                                                                                                        <el-option label="未激活" value="0" />
                                                                                                                                                                                      </el-select>
                                                                                                                                                                                    </el-form-item> -->

            <el-form-item>
              <el-button type="primary" :icon="Search" @click="handleQuery">搜索</el-button>
              <el-button :icon="Refresh" @click="resetQuery">重置</el-button>
            </el-form-item>
          </el-form>
        </div>

        <el-card shadow="never">
          <template #header v-if="true">
            <el-form-item style="float: left">
              <el-button type="success" :icon="Plus" @click="handleAdd">新增</el-button>
              <el-button type="danger" :icon="Delete" :disabled="ids.length === 0" @click="handleDelete">删除</el-button>
            </el-form-item>
          </template>

          <el-table v-loading="loading" :data="userList" @selection-change="handleSelectionChange">
            <el-table-column type="selection" align="center" width="50" />
            <el-table-column label="编号" column-key="id" align="center" prop="id" width="100" />
            <el-table-column label="用户名" column-key="username" align="center" prop="username" width="100" />
            <el-table-column label="性别" column-key="gender" align="center" prop="gender" width="100" />
            <el-table-column label="手机号码" column-key="cell" align="center" prop="cell" width="120" />
            <el-table-column label="是否激活" column-key="is_active" align="center" prop="is_active" width="100">

            </el-table-column>
            <el-table-column label="注册时间" column-key="date_joined" align="center" prop="date_joined" width="120" />

            <el-table-column label="操作" align="left" width="200">
              <template #default="scope">
                <el-button type="success" link @click="resetPassword(scope.row)">重置密码</el-button>
                <el-button type="primary" link @click="handleUpdate(scope.row)"
                  v-hasPerm="['sys:user:edit']">编辑</el-button>
                <el-button type="danger" link @click="handleDelete(scope.row)" v-hasPerm="['sys:user:del']">删除</el-button>
              </template>
            </el-table-column>
          </el-table>

          <pagination v-if="total > 0" :total="state.total" v-model:page="PagesParams.pageNum"
            v-model:limit="PagesParams.pageSize" @pagination="handleQuery" />
        </el-card>
      </el-col>
    </el-row>

    <!-- 新增用户表单 -->
    <el-dialog :title="dialog.title" v-model="dialog.visible" width="500px" append-to-body @close="closeDialog">
      <el-form ref="dataFormRef" :model="userAddFormData" :rules="rules" label-width="80px"
        style="width: 80%;margin: 0 auto;">
        <el-form-item label="用户名" prop="username">
          <el-input v-model="userAddFormData.username" placeholder="请输入用户名" />
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input v-model="userAddFormData.password" placeholder="请输入密码" />
        </el-form-item>
        <el-form-item label="手机号码" prop="cell">
          <el-input v-model="userAddFormData.cell" placeholder="请输入手机号码" maxlength="11" />
        </el-form-item>
        <el-form-item label="验证码" prop="code">
          <el-input v-model="userAddFormData.code" placeholder="请输入验证码" maxlength="6" style="width: 51%;" />
          <el-button :loading="state.loading" @click="handleSmsCode" :disabled="state.loading">
            {{ time == 60 ? "发送" : time + '秒' }}</el-button>
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="userAddFormData.email" placeholder="请输入邮箱" maxlength="50" />
        </el-form-item>
        <el-form-item label="状态" prop="status">
          <el-radio-group v-model="userAddFormData.status">
            <el-radio :label="1">激活</el-radio>
            <el-radio :label="0">未激活</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="用户性别" prop="gender">
          <el-select v-model="userAddFormData.gender" placeholder="请选择">
            <el-option label="保密" :value="0" />
            <el-option label="男" :value="1" />
            <el-option label="女" :value="2" />
          </el-select>
        </el-form-item>

      </el-form>
      <template #footer>
        <div class="dialog-footer">
          <el-button type="primary" @click="submitForm" :loading="state.loading" :disabled="state.loading">确 定</el-button>
          <el-button @click="closeDialog">取 消</el-button>
        </div>
      </template>
    </el-dialog>

  </div>
</template>
