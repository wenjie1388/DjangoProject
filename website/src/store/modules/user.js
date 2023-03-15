import { defineStore } from 'pinia';

import { ref } from 'vue';
import { setToken,getToken } from '../../utils/auth';
import { loginApi }  from '../../api/auth/index'

export const useUserStore = defineStore('user', () => {
    const acctoken = ref(getToken() || '');
    const id = ref('')
    const name = ref('');
    // const loading = ref(false);


    function login(loginData){
      return new Promise((resolve, reject)=>{
        loginApi(loginData)
        .then(response => {
          console.log('store',)
          const { Token,username } = response.data;
          acctoken.value = Token;
          // loading.value = true
          name.value = username
          setToken(Token);
          resolve();
        })
        .catch(error => {
          reject(error);
        });
      })
    }

    return {
      acctoken,
      name,
      // loading,
      login,
    }
})
// export  const useUserStore = defineStore('user',()=>{
//   state: () => ({
//     const token = ref(getCookies() || '');
//     const username = ref('');
//   }),
//   actions: {
//     async login(loginData) {
//     return new Promise((resolve, reject) => {
//       loginApi(loginData)
//         .then(response => {
//           const { accessToken } = response.data;
//           token.value = accessToken;
//           setToken(accessToken);
//           resolve();
//         })
//         .catch(error => {
//           reject(error);
//         });
//     });
//   }
//   },

  

  
  // 获取信息(用户昵称、头像、角色集合、权限集合)
  // function getInfo() {
  //   return new Promise((resolve, reject) => {
  //     getUserInfo()
  //       .then(({ data }) => {
  //         if (!data) {
  //           return reject('Verification failed, please Login again.');
  //         }
  //         if (!data.roles || data.roles.length <= 0) {
  //           reject('getUserInfo: roles must be a non-null array!');
  //         }
  //         nickname.value = data.nickname;
  //         resolve(data);
  //       })
  //       .catch(error => {
  //         reject(error);
  //       });
  //   });
  // }

  // 注销
  // function logout() {
  //   return new Promise((resolve, reject) => {
  //     logoutApi()
  //       .then(() => {
  //         resetRouter();
  //         resetToken();
  //         resolve();
  //       })
  //       .catch(error => {
  //         reject(error);
  //       });
  //   });
  // }

  // 重置
  // function resetToken() {
  //   removeToken();
  //   token.value = '';
  //   nickname.value = '';
  // }

//   return {
//     token,
//     username,
//   }
// })


// 非setup
export function useUserStoreHook() {
  return useUserStore(store);
}
