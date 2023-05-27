import { Captcha } from './../../api/auth/types';
import { infoForm } from './../../api/user/types';
// 系统依赖
import { defineStore } from 'pinia';
import { resetRouter } from '@/router';
import { store } from '@/store';
import { ref } from 'vue';

// utils/auth
import { getToken, setToken, removeToken, setId, getId, removeId } from '@/utils/auth';

// api/auth
import { loginApi, logoutApi,addCaptchaApi } from '@/api/auth';
// /api/user
import { getUserInfo, getAccountInfoAPI, updateUserInfoAPI, updateAccountInfoAPI } from '@/api/user';

// 数据类型依赖
import { LoginDataC,captchaEmailInfo,captchaPhoneInfo } from '@/api/auth/types';
import { UserInfo, AccountInfo,userInfo } from '@/api/user/types';

export const useUserStore = defineStore('user', () => {
  // state
  
  // 个人资料
  const id = ref<string>('');
  const nickname = ref<string>(''); // 网名

  const token = ref<string>(getToken() || '');
  const avatar = ref<string>(''); // 用户头像
  const active = ref<boolean>(false); // false=无法登录
  const status = ref<boolean>(false); // true=重新登录

  // 账号信息
  const password = ref<string>(''); // 密码
  const cellphone = ref<string>(''); // 手机
  const email = ref<string>(''); // 邮箱
  
  // 临时用的验证码
  const captcha =ref<string>(''); // 验证码

  // actions
  // 登录
  function login(loginData) {
    return new Promise<void>((resolve, reject) => {
      loginApi(loginData)
        .then((data) => {
          const { tokenType, accessToken } = data;
          token.value = tokenType + " " + accessToken; // Bearer eyJhbGciOiJIUzI1NiJ9.xxx.xxx
          id.value = data.id;
          getInfo(id.value);
          setToken(token.value);
          setId(id.value);
          resolve();
        })
        .catch(error => {
          reject(error);
        });
    });
  }

  // 获取个人资料(用户昵称、角色集合、权限集合)
  function getInfo() {
    return new Promise<UserInfo>((resolve, reject) => {
      getUserInfo('v1','01040201',id.value)
        .then((data) => {
          console.log(data)
          id.value = data.id;
          nickname.value = data.nickname;
          avatar.value = data.avatar;
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

  // 获取账号信息
  function getAccountInfo() { 
    return new Promise<UserInfo>((resolve, reject) => {
      getUserInfo('01040202',id.value)
        .then((data) => {
          password.value = data.password;
          email.value = data.email;
          cellphone.value = data.cellphone;
          resolve();
        })
        .catch((error) => { 
          reject(error);
        });
    })
  }

  /**
   * 获取验证码
   * @param captchaInfo 验证码参数
   * @returns 
   */
  function getCaptcha(account:string) { 
    return new Promise<UserInfo>((resolve, reject) => {
      addCaptchaApi(account)
        .then((data) => {
          captcha.value = data.captcha;
          resolve();
        })
        .catch((error) => { 
          reject(error);
        });
    });
  }

  /**
   * @param 修改个人资料
   * @param infoForm 个人资料表单
   * @returns 
   */
  function updateInfo(infoForm:userInfo) { 
    return new Promise<UserInfo>((resolve, reject) => {
      updateUserInfoAPI('01040401',id.value,infoForm)
        .then((data) => {
          id.value = data.id;
          nickname.value = data.nickname;
          resolve();
        })
        .catch((error) => { 
          reject(error);
        });
    })
  }

  /**
   * @param 修改账号信息
   * @param accountForm 账号信息表单
   * @returns 
   */
  function updateAccountInfo(accountForm:AccountInfo) { 
    return new Promise<UserInfo>((resolve, reject) => {
      updateUserInfoAPI('01040402',id.value,accountForm)
        .then((data) => {
          password.value = data.password;
          email.value = data.email;
          cellphone.value = data.cellphone;
          resolve();
        })
        .catch((error) => { 
          reject(error);
        });
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

  // 重置用户所有信息
  function resetUser() {
    removeToken();
    removeId();
    id.value = '';
    token.value = '';
    nickname.value = '';
    avatar.value = '';
    active.value = false;
    status.value = false;

    // account 
    password.value = '';
    cellphone.value = '';
    email.value = '';

    // 验证码
    captcha.value = '';
  }

  /**
   * @param 重置验证码
   */
  function resetCaptcha() {
    captcha.value = '';
  }



  return {
    id,
    token,
    avatar,
    nickname,
    active,
    status,

    // 账号信息 
    password,
    cellphone,
    email,

    // 验证码
    captcha,

    // 方法
    login,
    logout,
    
    resetUser,
    resetCaptcha,

    getInfo,
    getAccountInfo,
    getCaptcha,

    updateInfo,
    updateAccountInfo,
  };
});

// 非setup
export function useUserStoreHook() {
  return useUserStore(store);
}
