import request from '@/utils/request';
import { AxiosPromise } from 'axios';
import { ActivityRecommendationType } from "./types";


export function getActivityRecommendationApi(): AxiosPromise<ActivityRecommendationType> {
  return request({
    url: '/v1/activity/03020101',
    method: 'get',
  });
}