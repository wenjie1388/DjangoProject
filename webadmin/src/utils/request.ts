import axios, { AxiosRequestConfig, AxiosResponse } from 'axios';
import { ElMessage, ElMessageBox } from 'element-plus';
import { getToken } from '@/utils/auth';
import { useUserStoreHook } from '@/store/modules/user';
import { keysOf } from 'element-plus/es/utils';
import { AesEncryption } from './crypto';
import test from 'node:test';

// 创建 axios 实例
const service = axios.create({
  baseURL: import.meta.env.VITE_APP_BASE_API,
  timeout: 50000,
  headers: { 'Content-Type': 'application/json;charset=utf-8' }
});

// 请求拦截器
service.interceptors.request.use(
  (config: AxiosRequestConfig) => {
    if (!config.headers) {
      throw new Error(
        `Expected 'config' and 'config.headers' not to be undefined`
      );
    }
    const user = useUserStoreHook();
    if (user.token) {
      (config.headers as any).Authorization = getToken();
    };
    if (config.method == 'get') {
      var aes = new AesEncryption();
      for (var keys in config.params) {
        config.params[keys]=aes.encryptByAES(config.params[keys]);
      };
    };
    return config;
  },
  (error: any) => {
    return Promise.reject(error);
  }
);

// 响应拦截器
service.interceptors.response.use(
  (response: AxiosResponse) => {
    // const { code, msg } = response.data;
    // if (code === '200') {
    //   return response.data;
    // } else {
    //   // 响应数据为二进制流处理(Excel导出)
    //   if (response.data instanceof ArrayBuffer) {
    //     return response;
    //   }

    //   ElMessage({
    //     message: msg || '系统出错',
    //     type: 'error'
    //   });
    //   return Promise.reject(new Error(msg || 'Error'));
    // }
    return response
  },
  (error: any) => {
    if (error.response.data) {
      const { code, msg } = error.response.data;
      // token 过期,重新登录
      if (code === 'A0230') {
        ElMessageBox.confirm('当前页面已失效，请重新登录', '提示', {
          confirmButtonText: 'OK',
          type: 'warning'
        }).then(() => {
          localStorage.clear();
          window.location.href = '/';
        });
      } else {
        ElMessage({
          message: msg || '系统出错',
          type: 'error'
        });
      }
    }
    return Promise.reject(error.message);
  }
);

// 导出 axios 实例
export default service;
