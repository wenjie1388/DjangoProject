import { SmsCode } from './types';
/**
 * 登录数据类型（带验证码的）
 */
export interface LoginDataC {
  username: string;
  password: string;
  captcha: string;
}

/**
 * 注册数据类型（带验证码的）
 */
export interface registerDataC {
  username: string;
  password: string;
  checkPass: string;
  captcha: string;
}


/**
 * 登录数据类型（不带验证码的）
 */
export interface LoginData {
  username: string;
  password: string;
}



/**
 * Token 响应类型
 */
export interface TokenResult {
  Token: string;
  // refreshToken: string;
  // expires: number;
}

// 验证码参数之手机号码
export interface captchaPhoneInfo{
  cellphone: string;
}

/** 
 * @param 验证码参数之手机号码  
 */ 
export interface captchaPhoneInfo{
  cellphone: string;
}
/** 
 * @param 验证码参数之电子邮箱
 * 
 */ 
export interface captchaEmailInfo{
  email: string;
}

/**
 * 验证码类型
 */
export interface Captcha {
  captcha: string;
}

