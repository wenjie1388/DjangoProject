import { formContextKey } from "element-plus";




/**
 * 登录表单
 */
export interface LoginFormT {
  account: string;
  password: string;
}

/**
 * @param 登录-Response
 */
export interface LoginResponT {
    id: number;
    nickname: string;
    token: string;
}


/**
 * @param 注册表单
 */
export interface RegisterFormT {
  account: string;
  password: string;
}




/**
 * @param 用户信息
 */
export interface UserInfoT {
    address: string;
    avatar: string;
    cellphone: string;
    date_joined: string;
    email: string;
    id: number;
    id_card: string;
    introduction: string;
    is_activate: boolean;
    is_authenticated: boolean;
    last_login: string;
    male: string;
    name: string;
    password: string;
    username: string;
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













