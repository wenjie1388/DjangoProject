import request from '@/utils/request';
import { AxiosPromise } from 'axios';
import {  } from './types';


/**
 * 获取首页轮播图
 */
export function Carousel() { 
  request({
    url: '/api/v1/menus/' + ids,
    method: 'delete'
  });
}