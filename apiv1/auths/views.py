from rest_framework import status,mixins
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


import django_redis
import re
from django.conf import settings
from django.core.mail import send_mail
from .serializer import CreateCaptchaSerializer,verifyCaptchaSerializer
from utils.utils import get_auth_code_6


class CaptchaView(APIView):
  
  def get(self, request, *args, **kwargs):
    serializer = verifyCaptchaSerializer(data=request.query_params)
    serializer.is_valid(raise_exception=True)
    account = serializer.validated_data.get('account',None)
    captcha = serializer.validated_data.get('captcha',None)
    
    redis_conne = django_redis.get_redis_connection('verify_code')
    # 检验 verify_filter 是否过期。
    if redis_conne.ttl(account) == -2:
      return Response({'message':'验证码有误或已失效！'},status=status.HTTP_400_BAD_REQUEST)
    # 检验验证码是否匹配。
    if  redis_conne.get(account).decode() != captcha:
      return Response({'message':'验证码有误！'},status=status.HTTP_400_BAD_REQUEST)
        
    return Response({"message":"OK"},status=status.HTTP_200_OK)
  
  def post(self, request, *args, **kwargs):
    serializer = CreateCaptchaSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    captcha = get_auth_code_6()
    account = serializer.validated_data.get('account',None)
    redis_conne = django_redis.get_redis_connection('verify_code') 
    redis_conne.set(account,captcha,60*10)
    
    try :
      if re.search('@',account):
        # 向邮箱发送验证码
        self.send_mail_captcha(captcha,account)
      else:
        # 向手机发送验证码
        pass
    except :
      return Response({"message":"账号有误！"},status=status.HTTP_400_BAD_REQUEST)  
    return Response({"message":captcha},status=status.HTTP_200_OK)

  def send_mail_captcha(captcha,to_email,from_email=settings.EMAIL_HOST_USER):
    send_mail(
      subject='邮箱验证码',
      message='十分钟内有效！',
      from_email=from_email,
      recipient_list=[to_email],
      fail_silently=False,
      html_message=f'<p>验证码：{captcha} </p><p>十分钟内有效</p>'
      )
