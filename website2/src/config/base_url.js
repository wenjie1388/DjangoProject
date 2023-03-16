

let model = {
  //开发阶段接口地址
  dev: 'http://127.0.0.1:8000/api',
  //测试阶段接口地址
  test: 'http://127.0.0.1:8001/api',
  //发布阶段接口地址
  pro:'http://127.0.0.1:8002/api',
}

// 
export const BASE_URL = model.dev + '/v1'