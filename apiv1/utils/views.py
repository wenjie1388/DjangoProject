from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.status import (
    HTTP_200_OK,HTTP_201_CREATED,HTTP_202_ACCEPTED,HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,HTTP_401_UNAUTHORIZED,HTTP_406_NOT_ACCEPTABLE,
    HTTP_500_INTERNAL_SERVER_ERROR
)



import re
import django_redis 

from .utils import get_RandomString
from .serializer import CellphoneSerializer

''' 手机验证码接口 '''
@api_view(['GET'])
def SMSCodeView(request, *args, **kwargs):
    # 1. 序列化校验
    serializer = CellphoneSerializer(data=request.query_params)
    if not serializer.is_valid(raise_exception=True):
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    # 2. 接着生成验证码（6位，包含数字、字母），
    smscode = get_RandomString(6)
    # 4. 验证码存入 verify_code 数据库。验证码10分钟有效期
    redis_connec = django_redis.get_redis_connection('verify_code') 
    if not redis_connec.set(serializer.validated_data['cell'],smscode,60*10):
        # 保存 code 出错
        return Response({'msg':"数据库错误"},status=HTTP_500_INTERNAL_SERVER_ERROR)
    # 3. 通过 供应商 发送短信。
    # 4. 最后返回验证码。
    return Response({'SmsCode':smscode},status=HTTP_200_OK)