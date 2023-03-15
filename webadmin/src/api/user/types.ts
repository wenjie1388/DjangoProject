/**
 * 登录用户信息
 */
export interface UserInfo {
  nickname: string;
  avatar: string;
  roles: string[];
  perms: string[];
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
 * 用户查询参数
 */
export interface UserPages extends PageQuery {
  keywords: string;
  status: number;
}

/**
 * 用户列表项声明
 */
export interface UserListType {
  id: string;
  username: string;
  mobile: string;
  gender: number;
  is_active: number;
  date_joined: string;
}



/**
 * 员工分页列表项声明
 */
export interface StaffType {
  id: string;
  username: string;
  nickname: string;
  mobile: string;
  gender: number;
  avatar: string;
  email: string;
  status: number;
  deptName: string;
  roleNames: string;
  createTime: string;
}
/**
 * 用户分页项类型声明
 */
export type UserPageResult = PageResult<UserType[]>;



/**
 * 用户导入表单类型声明
 */
export interface UserImportData {
  deptId: number;
  roleIds: number[];
}

/**
 * 用户表单类型声明
 */
export interface UserForm {
  id: number | undefined;
  deptId: number;
  username: string;
  nickname: string;
  password: string;
  mobile: string;
  email: string;
  gender: number;
  status: number;
  remark: string;
  roleIds: number[];
}