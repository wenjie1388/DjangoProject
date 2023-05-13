
import random 
import string
import jwt

from django.conf import settings
from django.core.mail import send_mail


''' 以下是正则表达式 '''


username_re = r'^[a-zA-Z\u4e00-\u9fa5](?![0-9]+$)(?![a-zA-Z]+$)([a-z-A-Z0-9\u4e00-\u9fa5]{5,19}$)'
# password_re=r'^[a-zA-Z0-9][a-zA-Z_0-9@$!%*#~?&^]{5,19}$'
password_re=r'^[a-zA-Z](?![0-9]+$)(?![a-zA-Z]+$)(?![a-zA-Z0-9]+$)([a-z-A-Z0-9@,.!#~?&^]{5,23}$)'
cellphone_re = r'^1[3-9][0-9]{9}$'
# email_regex = r'^[\w]+@[\w]+.com$'
email_re = r'\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}'
auth_code_6_re=r'(?![a-zA-Z]{6})(?![0-9]{6})(^[a-zA-Z][0-9][a-zA-Z][0-9][a-zA-Z][0-9]$)'
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

def getRandomUsername():
    pass

def get_auth_code_6():
    letters = [random.choice(string.ascii_letters) for n in range(3)]
    digits = [random.choice(string.digits) for n in range(3)]
    authcode = ''
    for l,d in zip(letters,digits):
        authcode+=l
        authcode+=d
    return authcode

class JwtToken(object):
    
    def get_HS256(payload_):
        salt = settings.SECRET_KEY
        # 构造Header，默认如下
        headers = {'typ':'jwt','alg':'HS256'}
        return jwt.encode(headers=headers,payload=payload_,key=salt,algorithm='HS256')

def send_mail(subject, message, from_email, email, method='register' ,**kwargs):
    '''在大多数情况里，你可以使用 django.core.mail.send_mail() 来发送邮件。
    参数 subject, message, from_email 和 recipient_list 是必须的。
    subject: 一个字符串。
    message: 一个字符串。
    from_email ：字符串。如果为 None ，Django 将使用 DEFAULT_FROM_EMAIL 设置的值。
    recipient_list: 一个字符串列表，每项都是一个邮箱地址。recipient_list 中的每个成员都可以在邮件的 "收件人:" 中看到其他的收件人。
    fail_silently: 一个布尔值。若为 False， send_mail() 会在发生错误时抛出 smtplib.SMTPException 。可在 smtplib 文档找到一系列可能的异常，它们都是 SMTPException 的子类。
    auth_user: 可选的用户名，用于验证登陆 SMTP 服务器。 若未提供，Django 会使用 EMAIL_HOST_USER 指定的值。
    auth_password: 可选的密码，用于验证登陆 SMTP 服务器。若未提供， Django 会使用 EMAIL_HOST_PASSWORD 指定的值。
    connection: 可选参数，发送邮件使用的后端。若未指定，则使用默认的后端。查询 邮件后端 文档获取更多细节。
    html_message: 若提供了 html_message，会使邮件成为 multipart/alternative 的实例， message 的内容类型则是 text/plain ，并且 html_message 的内容类型是 text/html 。
    返回值会是成功发送的信息的数量（只能是 0 或 1 ，因为同时只能发送一条消息）。

    '''
    try:
        if method== 'register':
          username = kwargs['username']
          password = kwargs['password']
          send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=email,
            fail_silently=False,
            html_message=f'<p>用户名：{username}</p><p>密码：{password}</p>'
          )
        else:
          return 0
    except:
        return 0
    return 1

