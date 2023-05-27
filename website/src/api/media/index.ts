import request from '@/utils/request';
import { AxiosPromise } from 'axios';
import { CarouselType } from './types';


/**
 * 获取首页轮播图
 */
export function getCarouselAPI():AxiosPromise<CarouselType> { 
  return  request({
    url: '/v1/carousel',
    method: 'get'
  });
}