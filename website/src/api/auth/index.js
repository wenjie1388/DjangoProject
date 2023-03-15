import Axios from '../../utils/request.js';

/**
 * @param data {LoginForm}
 */
export function loginApi(data){
  return Axios({
    url: 'users/login',
    method: 'POST',
    data:data,
  });
}

/**
 * 注销
 */
export function logoutApi() {
  return Axios({
    url: '/api/v1/auth/logout',
    method: 'delete'
  });
}

/**
 * 获取验证码
 */
export function getCaptcha(){
  return Axios({
    url: '/captcha?t=' + new Date().getTime().toString(),
    method: 'get'
  });
}
