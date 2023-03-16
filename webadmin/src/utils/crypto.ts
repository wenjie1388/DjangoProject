import { encrypt, decrypt } from 'crypto-js/aes'
import { parse } from 'crypto-js/enc-utf8'
import pkcs7 from 'crypto-js/pad-pkcs7'
import ZeroPadding from 'crypto-js'
import ECB from 'crypto-js/mode-ecb'
import UTF8 from 'crypto-js/enc-utf8'


export class AesEncryption {

  private key
  private iv

  constructor(key = '1111111111000000', iv = '0000001111111111') {
    this.key = parse(key)
    this.iv = parse(iv)
  }

  get getOptions() {
    return {
      mode: BCB,
      padding: ZeroPadding,
      iv: this.iv,
    }
  }

  encryptByAES(text: string) {
    return encrypt(text, this.key, this.getOptions).toString()
  }

  decryptByAES(text: string) {
    return decrypt(text, this.key, this.getOptions).toString(UTF8)
  }
}


