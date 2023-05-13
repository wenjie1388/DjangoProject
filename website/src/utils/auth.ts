import Cookies from 'js-cookie';

const TokenKey = 'token';
const IdKey = "id"
export function getToken() {
  return Cookies.get(TokenKey);
}

export function setToken(token: string) {
  Cookies.set(TokenKey, token);
}

export function removeToken() {
  return Cookies.remove(TokenKey);
}


export function getId() {
  return Cookies.get(IdKey);
}

export function setId(id: string) {
  Cookies.set(IdKey, id);
}

export function removeId() {
  return Cookies.remove(IdKey);
}

