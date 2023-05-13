import { defineStore } from 'pinia';

import { getToken, setToken, removeToken,setId,getId,removeId } from '@/utils/auth';
import { loginApi, logoutApi } from '@/api/auth';
import { getUserInfo } from '@/api/user';
import { resetRouter } from '@/router';
import { store } from '@/store';
import { LoginDataC } from '@/api/auth/types';
import { ref } from 'vue';
import { UserInfo } from '@/api/user/types';

export const useUserStore = defineStore('user', () => {
  // state
  const id = ref<string>('');
  const token = ref<string>(getToken() || '');
  const nickname = ref<string>(''); // 网名
  const password = ref<string>(''); // 密码
  const avatar = ref<string>(''); // 用户头像
  const cellphone = ref<string>(''); // 手机
  const email = ref<string>(''); // 邮箱
  const active = ref<boolean>(false); // false=无法登录
  const status = ref<boolean>(false); // true=重新登录

  // actions
  // 登录
  function login(loginData: LoginDataC) {
    return new Promise<void>((resolve, reject) => {
      loginApi(loginData)
        .then((data) => {
          const { tokenType, accessToken } = data;
          token.value = tokenType + " " + accessToken; // Bearer eyJhbGciOiJIUzI1NiJ9.xxx.xxx
          id.value = data.id
          setToken(token.value);
          setId(id.value);
          resolve();
        })
        .catch(error => {
          reject(error);
        });
    });
  }

  // 获取简洁信息(用户昵称、角色集合、权限集合)
  function getInfo() {
    return new Promise<UserInfo>((resolve, reject) => {
      getUserInfo()
        .then((data) => {
          console.log(data)
          id.value = data.id;
          nickname.value = data.nickname;
          avatar.value = data.avatar;
          cellphone.value = data.cellphone;
          email.value = data.email;
          active.value = data.active;
          status.value = data.status;
          console.log(data.id,data.nickname)
          resolve(data);
        })
        .catch(error => {
          reject(error);
        });
    });
  }

  function getAccountInfo() {
    return new Promise<UserInfo>((resolve, reject) => {
      
    })
  }
  // 注销
  function logout() {
    return new Promise<void>((resolve, reject) => {
      logoutApi(id.value)
        .then(() => {
          resetRouter();
          resetUser();
          resolve();
        })
        .catch(error => {
          reject(error);
        });
    });
  }

  // 重置
  function resetUser() {
    removeToken();
    removeId();
    id.value = '';
    token.value = '';
    nickname.value = '';
    avatar.value = '';
    cellphone.value = '';
    email.value = '';
    active.value = false;
    status.value = false;
  }




  return {
    id,
    token,
    avatar,
    nickname,
    cellphone,
    email,
    active,
    status,
    login,
    getInfo,
    logout,
    resetUser
  };
});

// 非setup
export function useUserStoreHook() {
  return useUserStore(store);
}
