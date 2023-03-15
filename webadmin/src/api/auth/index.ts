import request from '@/utils/request';
import { AxiosPromise } from 'axios';
import { LoginData, TokenResult, VerifyCode } from './types';

/**
 *
 * @param data {LoginForm}
 * @returns
 */
export function loginApi(paramsData: LoginData): AxiosPromise<TokenResult> {
  return request({
    url: 'v1/user/adminuser/login',
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
 * 获取图片验证码
 */
export function getCaptcha(): AxiosPromise<VerifyCode> {
  return request({
    url: '/captcha?t=' + new Date().getTime().toString(),
    method: 'get'
  });
}

/**
 * 获取手机验证码
 */
export function getSmsCaptcha(cell:string): AxiosPromise<VerifyCode> {
  return request({
    url: '/v1/utils/smscode',
    method: 'get',
    params:{'cell':cell}
  });
}
