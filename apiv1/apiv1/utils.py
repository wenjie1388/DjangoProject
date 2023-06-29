from django.conf import settings
from django.core.mail import send_mail

async def send_mail_captcha(captcha,to_email,from_email=settings.EMAIL_HOST_USER):

  await send_mail(
  subject='邮箱验证码',
  message='十分钟内有效！',
  from_email=from_email,
  recipient_list=[to_email],
  fail_silently=False,
  html_message=f'<p>验证码：{captcha} </p><p>十分钟内有效</p>'
  )

