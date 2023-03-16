import base64
from Crypto.Cipher import AES

class CryptoAES(object):
    
    def __init__(self,key,iv):
        '''
        构建一个AES对象
        key: 秘钥，字节型
        mode: 使用模式，只提供两种，AES.MODE_CBC, AES.MODE_ECB
        iv： iv偏移量，字节型数据
        paddingMode: 填充模式，默认为NoPadding, 可选NoPadding，ZeroPadding，PKCS5Padding，PKCS7Padding
        characterSet: 字符集编码
        '''
        self.key = key
        self.iv = iv
        self.size = 16
        self.mode = 'CBC'
        self.paddingMode = 'ZeroPadding'
        self.characterSet = 'utf-8'

    def ZeroPadding(self,plaintext):
        t= len(plaintext) % self.size
        return plaintext + b'\x00'*(self.size-t)  
    

    # 将明文用AES加密
    def encode(self,plaintext):
        '''
        plaintext：明文，字符串
        '''
        plaintext_byte = plaintext.encode(self.characterSet)
        if len(plaintext_byte) % self.size != 0:
            if self.paddingMode == 'ZeroPadding':
                plaintext_byte=self.ZeroPadding(plaintext_byte)
        # 创建加密对象
        AES_obj = AES.new(self.key, AES.MODE_CBC, self.iv)
        # 完成加密
        AES_en_str = AES_obj.encrypt(plaintext_byte)
        # 用base64编码一下
        AES_en_str = base64.b64encode(AES_en_str)
        # 最后将密文转化成字符串
        AES_en_str = AES_en_str.decode(self.characterSet)
        return AES_en_str

    #  ciphertext
    def decode(self,ciphertext):
        # 解密过程逆着加密过程写
        # 将密文字符串重新编码成二进制形式
        data = ciphertext.encode(self.characterSet)
        # 将base64的编码解开
        data = base64.decodebytes(data)
        # 创建解密对象
        AES_de_obj = AES.new(self.key, AES.MODE_CBC, self.iv)
        # 完成解密
        AES_de_str = AES_de_obj.decrypt(data)
        # 对明文解码
        AES_de_str = AES_de_str.decode(self.characterSet)
        # 去掉补上的空格
        if self.paddingMode == 'ZeroPadding':
          print(type(AES_de_str))
          AES_de_str = AES_de_str.rstrip('\x00')
        return AES_de_str
    

    def encodeDict(self,data):
        for key,value in data.items():
          data[key]=self.encode(value)
        return data
    
    def decodeDict(self,data):
        for key,value in data.items():
          data[key]=self.decode(value)
        return data
    

            
    

 
 
 