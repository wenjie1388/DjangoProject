from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.status import (
    HTTP_200_OK,HTTP_201_CREATED,HTTP_202_ACCEPTED,HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,HTTP_401_UNAUTHORIZED,HTTP_406_NOT_ACCEPTABLE,
    HTTP_500_INTERNAL_SERVER_ERROR
)

from redis.exceptions import ConnectionError,ResponseError
import re
import django_redis 

from .tasks import send_mail_code
from .utils import get_RandomString,get_auth_code_6
from .serializer import CellphoneSerializer,EmailSerializer

''' 手机验证码接口 '''
@api_view(['GET'])
def SMSCodeView(request):
    # 1. 序列化校验
    serializer = CellphoneSerializer(data=request.query_params)
    serializer.is_valid(raise_exception=True)

    # 2. 接着生成验证码
    smscode = get_auth_code_6()
    is_save = serializer.validated_data.get('is_save',None)
    try:
      # 4. 验证码存入 verify_code 数据库。验证码10分钟有效期
      redis_connec = django_redis.get_redis_connection('verify_code') 
      redis_connec.set(serializer.validated_data['cell'],smscode,60*10)
    except ConnectionError:
      return Response({'msg':"ConnectionError：无法连接 redis "},status=HTTP_500_INTERNAL_SERVER_ERROR)
    except ResponseError:
      Response({'msg':["ResponseError：redis 启动保护模式 "]},status=HTTP_500_INTERNAL_SERVER_ERROR)
    # if is_save == True :
      # 3. 通过 供应商 发送短信。
      # pass
    # 4. 最后返回验证码。
    return Response({'SmsCode':[smscode]},status=HTTP_200_OK)

''' 邮箱验证码接口 '''
@api_view(['GET'])
def EmailCodeView(request, *args, **kwargs):
    # 1. 序列化校验
    serializer = EmailSerializer(data=request.query_params)
    if not serializer.is_valid(raise_exception=True):
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    # 2. 接着生成验证码
    email = serializer.validated_data['email']
    emailcode = get_auth_code_6()
    try:
      # 4. 验证码存入 verify_code 数据库。验证码10分钟有效期
      redis_connec = django_redis.get_redis_connection('verify_code') 
      redis_connec.set(email,emailcode,60*10)
    except ConnectionError:
      Response({'msg':["无法连接 redis "]},status=HTTP_500_INTERNAL_SERVER_ERROR)
    except ResponseError:
      Response({'msg':[" redis 启动保护模式 "]},status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    # 3. 通过 异步calay 发送邮件。
    # if not send_mail_code(emailcode,email):
    #     return Response({'msg':[f"{email}不存在"]},status=HTTP_400_BAD_REQUEST)
    # 4. 最后返回验证码。
    return Response({'emailcode':[emailcode]},status=HTTP_200_OK)



# class 