import axios from 'axios';
import { BASE_URL } from '../config/base_url';
import COOKIES from 'js-cookie'

const Axios = axios.create({
  baseURL: BASE_URL,
  timeout: 1000 * 60 * 3,
  headers: {
    // 'X-Custom-Header': 'axios',
  }
});

// 请求拦截器
Axios.interceptors.request.use(
  (config) => {
    // console.log("interceptors.request");
    // let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
    // config.headers['csrftoken'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1];

    return config;
  },
  (error) => {
    return Promise.reject(error);
  });

// 响应拦截器
Axios.interceptors.response.use(
  (response) => {
    const { code, msg } = response.data;
    console.log(response.headers)
    return response;
  },
  (error) => Promise.reject(error),
);


export default Axios;