import { defineStore } from 'pinia';

import { getToken, setToken, removeToken } from '@/utils/auth';
import { loginApi, logoutApi } from '@/api/auth';
import { getUserInfo } from '@/api/user';
import { resetRouter } from '@/router';
import { store } from '@/store';
import { LoginData } from '@/api/auth/types';
import { ref } from 'vue';
import { UserInfo } from '@/api/user/types';

export const useUserStore = defineStore('user', () => {
  // state
  const token = ref<string>(getToken() || '');
  const id = ref<string>('');
  const username = ref<string>(''); // 用户名
  const name = ref<string>('');     // 姓名
  const avatar = ref<string>(''); // 用户头像
  const joined = ref<string>(''); // 注册时间
  // const roles = ref<Array<string>>([]); // 用户角色编码集合 → 判断路由权限
  // const perms = ref<Array<string>>([]); // 用户权限编码集合 → 判断按钮权限
  const status = ref<string>(''); // 用户激活权限 → 判断路由权限
  const active = ref<boolean>(false); // 用户激活权限 → 判断路由权限
  const staff = ref<boolean>(false); // 用户职工权限 → 判断组件权限
  const admin = ref<boolean>(false); // 用户管理员权限 → 判断按钮权限  

  // actions
  // 登录
  function login(loginData: LoginData) {
    return new Promise<void>((resolve, reject) => {
      loginApi(loginData)
        .then((response) => {
          if (response.status != 200) {
            reject(response.data['msg']);
          }else{
            const { Id,Username, Token } = response.data;
            token.value = Token;
            id.value = Id;
            username.value = Username;
            setToken(Token);
            resolve();
          }
        })
        .catch(error => {
          reject(error);
        });
    });
  }

  // 获取信息(用户昵称、角色集合、权限集合)
  function getInfo(id: string) {
    return new Promise<UserInfo>((resolve, reject) => {
      getUserInfo(id)
        .then(response => {
          const { Name, Avatar, Active, Staff, Admin, Joined, Status } = response.data;
          joined.value = Joined;
          avatar.value = Avatar;
          active.value = Active;
          staff.value = Staff;
          admin.value = Admin;
          name.value = Name;
          status.value = Status;
          resolve(response.data);
        })
        .catch(error => {
          reject(error);
        });
    });
  }

  // 注销
  function logout() {
    return new Promise<void>((resolve, reject) => {
      logoutApi(id.value)
        .then(() => {
          resetRouter();
          resetToken();
          resolve();
        })
        .catch(error => {
          reject(error);
        });
    });
  }

  // 重置
  function resetToken() {
    removeToken();
    token.value = '';
    id.value = '';
    name.value = '';
    avatar.value = '';
    active.value = false;
    staff.value = false;
    admin.value = false;
    joined.value = '';
    name.value = '';
    status.value = '';
  }
  return {
    token,
    id,
    username,
    avatar,
    active,
    staff,
    joined,
    name,
    status,
    admin,
    login,
    getInfo,
    logout,
    resetToken
  };
});

// 非setup
export function useUserStoreHook() {
  return useUserStore(store);
}
