import request from '@/utils/request';
import { AxiosPromise } from 'axios';
import { UserForm, userInfo,UpdateUserInfo,AccountInfo, UserPageResult, UserQuery } from './types';

/**
 * 获取用户简洁的信息（昵称、头像、权限集合和角色集合）
 */
export function getUsersInfo(): AxiosPromise<UserInfo> {
  return request({
    url: '/v1/users',
    method: 'get'
  });
}

/**
 * 获取指定用户的指定信息
 * @param path_id 01040201:用户简易信息；01040203:获取用户电子名片
 * @param  v_id:APi版本
 * @param u_id:用户id
 * @returns 
 */
export function getUserInfo(v_id:string,path_id:string,uid:string|string[]){
  return request({
    url: '/'+v_id+ '/users/'+path_id+'/'+uid,
    method: 'get',
  });
}


/**
 * 获取用户查询列表
 */
export function queryUserList(queryParams: UserQuery): AxiosPromise<UserPageResult> {
  return request({
    url: '/v1/users/',
    method: 'get',
    params: queryParams
  });
}

/**
 * 更新用户信息
 * @param path_id 01040401:个人资料； 01040402:账号信息
 * @param u_id 用户id
 * @param updateForm 更新表单
 * @returns 
 */
export function updateUserInfoAPI(path_id:string,u_id:string,updateForm:object): AxiosPromise {
  return request({
    url: '/v1/users/'+path_id + '/' +u_id,
    method: 'update',
    data: updateForm,
  });
}

/**
 * @param 用户动作API 
 * @param path_id：010501：点赞，010502：收藏 ；uid 用户id
 * @returns 
 */
export function userActionApi(path_id:string,u_id: string) {
  return request({
    url: '/v1/users/'+path_id+'/'+u_id,
    method: 'get',
  });
}

