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
// user API
import {
  getUserInfoApi,
  getAccountInfoAPI,
  patchUserInfoApi,
  updateAccountInfoAPI
} from '@/api/user';

// 数据类型依赖
import { LoginDataC,captchaEmailInfo,captchaPhoneInfo } from '@/api/auth/types';
import { UserInfo, AccountInfo,userInfo } from '@/api/user/types';

export const useUserStore = defineStore('user', () => {
  // state
  
  // 个人资料
  const id = ref<number>('');
  const nickname = ref<string>('');
  const male = ref<string>(''); // 性别
  const introduction = ref<string>('');
  const address = ref<string>('');
  const avatar = ref<string>(''); // 用户头像

  // 权限信息
  const token = ref<string>(getToken() || '');
  const is_activate = ref<boolean>(true); // True-账号已激活，能登录；反之则不能登录
  const status = ref<boolean>(false); // true=重新登录

  // 账号信息
  const password = ref<string>(''); // 密码
  const cellphone = ref<string>(''); // 手机
  const email = ref<string>(''); // 邮箱
  
  // 实名认证
  const is_authenticated= ref<boolean>(false); // True-通过实名验证；
  const name = ref<string>(''); // 姓名
  const id_card= ref<string>('');  // 身份证号

  // 辅助信息
  const captcha = ref<string>(''); // 验证码
  const last_login = ref<string>('');
  const date_joined = ref<string>('');
  

  // actions
  // 登录
  function login(version,LoginForm) {
    return new Promise<void>((resolve, reject) => {
      loginApi(version,LoginForm)
        .then((data) => {
          const { id, nickname, token } = data;
          console.log(data.id);
          token.value = token; // Bearer eyJhbGciOiJIUzI1NiJ9.xxx.xxx
          id.value = id;
          nickname.value = nickname;
          setToken(token.value);
          resolve();
        })
        .catch(error => {
          reject(error);
        });
    });
  }

  // 获取个人资料(用户昵称、角色集合、权限集合)
  function getInfo(version,) {
    return new Promise<void>((resolve, reject) => {
      getUserInfoApi(version,id.value)
        .then((data) => {
          console.log(data.male)
          male.value = data.male;
          introduction.value = data.introduction;
          address.value = data.address;
          is_activate.value = data.is_activate;
          status.value = data.status;
          password.value = data.password;
          cellphone.value = data.cellphone;
          email.value = data.email;
          is_authenticated.value = data.is_authenticated;
          name.value = data.name;
          id_card.value = data.id_card;
          date_joined.value = data.date_joined;
          last_login.value = data.last_login;
          resolve(data);
        })
        .catch(error => {
          reject(error);
        });
    });
  }

  /**
   * 生成验证码
   * @param captchaInfo 验证码参数
   * @returns 
   */
  function getCaptcha(account:string) { 
    return new Promise<void>((resolve, reject) => {
      addCaptchaApi(account)
        .then((data) => {
          const { message } = data;
          captcha.value = message;
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
      updateUserInfoApi('01040402',id.value,accountForm)
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

  function updateProfile(dataForm) {
    return new Promise<UserInfo>((resolve, reject) => { 
      patchUserInfoApi('010601',id.value,dataForm)
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
