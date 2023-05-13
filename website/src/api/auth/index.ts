import request from '@/utils/request';
import { AxiosPromise } from 'axios';
import { LoginDataC, TokenResult, VerifyCode,Captcha } from './types';

/**
 *
 * @param data {LoginForm}
 * @returns
 */
export function loginApi(paramsData: LoginDataC): AxiosPromise<TokenResult> {
  return request({
    url: 'v1/users/login',
    method: 'get',
    params: paramsData
  });
}

/**
 * 注销
 */
export function logoutApi(id:string) {
  return request({
    url: 'v1/users/logout/'+id,
    method: 'delete'
  });
}

/**
 * 获取6位的验证码
 */
export function getCaptchaApi(username:string): AxiosPromise<Captcha> {
  return request({
    url: '/v1/auth/captcha',
    method: 'get',
    params: {
      'username': username
    },
  });
}


