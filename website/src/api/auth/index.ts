import request from '@/utils/request';
import { AxiosPromise } from 'axios';
import { LoginDataC, TokenResult, VerifyCode,Captcha,captchaEmailInfo,captchaPhoneInfo } from './types';

/**
 * 登录接口
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
 * 注销接口
 */
export function logoutApi(id:string) {
  return request({
    url: 'v1/users/logout/'+id,
    method: 'delete'
  });
}

/**
 * 注销接口
 */
export function exitApi(id:string) {
  return request({
    url: 'v1/users/exit/'+id,
    method: 'get'
  });
}

/**
 * 校验验证码
 * @param verify 校验字段
 * @param captcha 验证码
 * @returns 
 */
export function verifyCaptchaApi(verify:string,captcha:string): AxiosPromise<void> {
  return request({
    url: '/v1/auth/captcha',
    method: 'get',
    params: {
      'verify':verify,
      'captcha': captcha,
    },
  });
}



/**
 * @param 生成 6 位验证码
 */
export function addCaptchaApi(account:string): AxiosPromise<Captcha> {
  return request({
    url: '/v1/auth/captcha',
    method: 'post',
    data: {
      'account': account
    },
  });
}

