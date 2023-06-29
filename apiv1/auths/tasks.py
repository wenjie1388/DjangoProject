from celery import Celery

from django.conf import settings
from django.core.mail import send_mail

# app = Celery('tasks', broker=settings.REDIS10_LOCATION)
app = Celery('tasks', broker='redis://192.168.139.129:6379/10')


@app.task
def send_mail_to_adminuser(name,pw,to_email,from_email=None):

    if from_email is None:
        from_email=settings.EMAIL_HOST_USER
    try:
        send_mail(
        subject='管理员账号',
        message='请把密码妥善保管或及时更改密码！',
        from_email=from_email,
        recipient_list=to_email,
        fail_silently=False,
        html_message=f'<p>用户名：{name}</p><p>密码：{pw}</p>'
        )
    except:
        return 0
    return 1

@app.task
def send_mail_code(emailcode,to_email,from_email=None):

    if from_email is None:
        from_email=settings.EMAIL_HOST_USER
    try:
        send_mail(
        subject='邮箱验证码',
        message='十分钟内有效！',
        from_email=from_email,
        recipient_list=[to_email],
        fail_silently=False,
        html_message=f'<p>验证码：{emailcode} </p><p>十分钟内有效</p>'
        )
    except:
        return 0
    return 1








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