import request from '@/utils/request';
import { AxiosPromise } from 'axios';
import {
  UserForm,
  UserInfoT,
  UpdateUserInfo,
  AccountInfo,
  UserPageResult,
  UserQuery
} from './types';
import { 
  LoginForm,
  LoginResponT

} from './types';


/**
 * 登录接口
 * @param data {LoginForm}
 * @returns
 */
export function loginApi(version,paramsData: LoginForm): AxiosPromise<LoginResponT> {
  return request({
    url: '/'+version+'/users/login/',
    method: 'get',
    params: paramsData
  });
}




/**
 * 获取用户信息
 * @param uid:用户id
 */
export function getUserInfoApi(version:string,uid:number): AxiosPromise<UserInfoT> {
  return request({
    url: '/'+version+'/users/'+uid+'/',
    method: 'get'
  });
}


/**
 * 更新用户信息
 * @param uid 用户id
 * @param updateForm 更新表单
 * @param version API版本
 * @returns 
 */
export function updateUserInfoApi(version:string,uid:number,updateForm:object): AxiosPromise {
  return request({
    url: '/'+version+'/users/'+uid +'/',
    method: 'patch',
    data: dataForm,
  });
}



/**
 * 删除用户接口
 * @param uid 用户id
 * @param version API版本
 * @returns 
 */
export function deleteUserApi(version:string,uid:number) {
  return request({
    url: '/'+version+'/users/'+uid+'/',
    method: 'delete'
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








