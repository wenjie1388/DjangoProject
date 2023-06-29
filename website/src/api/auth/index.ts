import request from '@/utils/request';
import { AxiosPromise } from 'axios';
import { LoginDataC, TokenResult, VerifyCode,Captcha,captchaEmailInfo,captchaPhoneInfo } from './types';


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
export function createCaptchaApi(version:string,account:string): AxiosPromise<Captcha> {
  return request({
    url: '/'+version+'/auths/captcha',
    method: 'post',
    data: {
      'account': account
    },
  });
}

