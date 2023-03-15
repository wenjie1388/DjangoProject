
import random 
import string
import jwt

username_re = r'^[a-zA-Z\u4e00-\u9fa5](?![0-9]+$)(?![a-zA-Z]+$)([a-z-A-Z0-9\u4e00-\u9fa5]{5,19}$)'
# password_re=r'^[a-zA-Z0-9][a-zA-Z_0-9@$!%*#~?&^]{5,19}$'
password_re=r'^[a-zA-Z](?![0-9]+$)(?![a-zA-Z]+$)(?![a-zA-Z0-9]+$)([a-z-A-Z0-9@,.!#~?&^]{5,23}$)'
cellphone_re = r'^1[3-9][0-9]{9}$'
# email_regex = r'^[\w]+@[\w]+.com$'
email_re = r'\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}'
randomStr6_re=r'(?![a-zA-Z]{6})(?![0-9]{6})(^[0-9a-zA-Z]{6}$)'
smscode_re= r'^(?![0-9]+$)(?![a-zA-Z]+$)([a-z-A-Z0-9]{6}$)'
gender_re = r'^[MF]{1}$'


def get_RandomString(length):
    ''' 获取 length 长度的随机字符串 包括数字、字母'''
    # SystemRandom类提供了所有的随机数产生方法的random模块本身呢，用相同的含义，只是使用加密RNG实现它们。
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length))

def get_RandomPassword(length):
    ''' 获取 length 长度的随机密码 包括数字、字母'''
    T1 = random.choice(string.ascii_letters)
    T2 = get_RandomString(length-2)
    T3 = random.choice('@,.!#~?&^')
    return ''.join([T1,T2,T3])




def get_JwtToken():
    pass



