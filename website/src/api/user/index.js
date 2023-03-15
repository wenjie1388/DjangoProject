import Axios from '../../utils/request';

/**
 * 获取用户信息（昵称、头像、阅读量、点赞量、访问量）
 */
export function getUserInfo(userId){
  return Axios({
    url: '/api/v1/users'+userId,
    method: 'get'
  });
}

/**
 * 获取用户分页列表
 *
 * @param queryParams
 */
export function listUserPages(queryParams){
  return Axios({
    url: '/api/v1/users/pages',
    method: 'get',
    params: queryParams
  });
}

/**
 * 获取用户表单详情
 *
 * @param userId
 */
export function getUserForm(userId){
  return Axios({
    url: '/api/v1/users/' + userId + '/form',
    method: 'get'
  });
}

/**
 * 添加用户
 *
 * @param data
 */
export function addUser(data) {
  return Axios({
    url: '/api/v1/users',
    method: 'post',
    data: data
  });
}

/**
 * 修改用户
 *
 * @param id
 * @param data
 */
export function updateUser(id, data) {
  return Axios({
    url: '/api/v1/users/' + id,
    method: 'put',
    data: data
  });
}

/**
 * 修改用户状态
 *
 * @param id
 * @param status
 */
export function updateUserStatus(id, status) {
  return Axios({
    url: '/api/v1/users/' + id + '/status',
    method: 'patch',
    params: { status: status }
  });
}

/**
 * 修改用户密码
 *
 * @param id
 * @param password
 */
export function updateUserPassword(id, password) {
  return Axios({
    url: '/api/v1/users/' + id + '/password',
    method: 'patch',
    params: { password: password }
  });
}

/**
 * 删除用户
 *
 * @param ids
 */
export function deleteUsers(ids) {
  return Axios({
    url: '/api/v1/users/' + ids,
    method: 'delete'
  });
}

/**
 * 下载用户导入模板
 *
 * @returns
 */
export function downloadTemplate() {
  return Axios({
    url: '/api/v1/users/template',
    method: 'get',
    responseType: 'arraybuffer'
  });
}

/**
 * 导出用户
 *
 * @param queryParams
 * @returns
 */
export function exportUser(queryParams) {
  return Axios({
    url: '/api/v1/users/_export',
    method: 'get',
    params: queryParams,
    responseType: 'arraybuffer'
  });
}

/**
 * 导入用户
 *
 * @param file
 */
export function importUser(deptId, roleIds, file) {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('deptId', deptId.toString());
  formData.append('roleIds', roleIds);
  return Axios({
    url: '/api/v1/users/_import',
    method: 'post',
    data: formData,
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  });
}
