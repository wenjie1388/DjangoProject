/**
 * 登录用户信息
 */
export interface UserInfo {
  nickname: string;
  avatar: string;
  active: boolean;
  status: boolean;
}


/**
 * 个人资料参数
 */
export interface UserInfo{
  id: string;
  nickname: string;
}

/**
 * 用户的账号信息参数
 */
export interface AccountInfo{
  id:string;
  password: string;
  cellphone: string;
  email: string;
}

/**
 * 用户查询参数
 */
export interface UserQuery {
  username: string;
  // active: string;
  pageNum: number;
  pageSize: number;
}

/**
 * 用户查询参数类型声明
 */
export interface UserQuery2 {
  id: string;
  username: string;
  gender: string;
  cell: string;
  active: string;
  date_joined: string;
  pageNum: number;
  pageSize: number;
}

/**
 * 新增用户表单类型声明
 */
export interface UserAddForm {
  username: string;
  password: string;
  cell: string;
  email: string;
  code: string;
  gender: number;
  status: number;
}


/**
 * 电子名片
 */
export interface userCardType {
  avatar: string;
  collect: number;
  count: number;
  id: string; 
  nickname: string;
  pageviews: number;
  upvote: number;
  introduction: string;
}













