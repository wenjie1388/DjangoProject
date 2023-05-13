import axios, { AxiosRequestConfig, AxiosResponse } from 'axios';
import { ElMessage, ElMessageBox } from 'element-plus';
import { getToken } from '@/utils/auth';
import { useUserStoreHook } from '@/store/modules/user';
import { keysOf } from 'element-plus/es/utils';
import { AesEncryption } from './crypto';
import test from 'node:test';

// 创建 axios 实例
const service = axios.create({
  // baseURL: import .meta.env.VITE_APP_BASE_API,
  baseURL: "http://127.0.0.1:4523/m1/2691554-0-default",

  timeout: 50000,
  headers: { 'Content-Type': 'application/json;charset=utf-8' }
});

// 请求拦截器
service.interceptors.request.use(
  (request: AxiosRequestConfig) => {
    if (!request.headers) {
      throw new Error(
        `Expected 'config' and 'config.headers' not to be undefined`
      );
    }
    const user = useUserStoreHook();
    if (user.token) {
      (request.headers as any).Authorization = getToken();
    };
    return request;
  },
  (error: any) => {
    return Promise.reject(error);
  }
);

// 响应拦截器
service.interceptors.response.use(
  (response: AxiosResponse) => {
    const { status,statusText } = response;
    if (status == '200') {
      return response.data;
    } else {
      ElMessage({
        message: '系统出错',
        type: 'error'
      });
      return Promise.reject(new Error( statusText));
    }
  },
  (error: any) => {
    return Promise.reject(error);
  }
);

// 导出 axios 实例
export default service;
