from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
import django_redis
import re

from .serializer import CreateCaptchaSerializer
from utils.utils import get_auth_code_6


class CaptchaView(GenericAPIView):
  
  def get(self,request):
    return Response('aaa')
  
  def post(self,request):
    serializer = CreateCaptchaSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    captcha = get_auth_code_6()
    account = serializer.validated_data.get('account')
    redis_conne = django_redis.get_redis_connection('verify_code') 
    redis_conne.set(account,captcha,60*10)
    if re.search('@',account):
      # 向邮箱发送验证码
      pass
    else:
      # 向手机发送验证码
      pass
    return Response({"message":captcha},status=status.HTTP_200_OK)
    
    
    
    
    
    
    pass
  
