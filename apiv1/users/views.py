from django.contrib.auth import views

from django.conf import settings
from django.core.cache import cache
from django.contrib.auth.hashers import check_password,make_password
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt,csrf_protect

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,RetrieveDestroyAPIView
from rest_framework.status import (
    HTTP_200_OK,HTTP_201_CREATED,HTTP_202_ACCEPTED,HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,HTTP_401_UNAUTHORIZED,HTTP_404_NOT_FOUND,HTTP_406_NOT_ACCEPTABLE,
    HTTP_500_INTERNAL_SERVER_ERROR
)
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.settings import api_settings
from rest_framework import authentication, permissions,mixins
from rest_framework import generics


import jwt,datetime,django_redis 
from .models import AnyUser as User,AdminUser
from .serializers import LoginSerializer,EmailRegistererializer,CellRegistererializer,UserListSerializer,CreateSerializer
from .exceptions import UserAlreadyExists
from utils.crypto import CryptoAES


@api_view(['get'])
def AnyUserLogin(self,request,*args,**kwargs):
    ''' Any用户登录 '''
    # aes = CryptoAES(b'1111111111000000',b'0000001111111111')
    # query_params = {'username':request.query_params['username'],'password':request.query_params['password']}
    # query_params = aes.decodeDict(query_params)
    # serializer = LoginSerializer(data=query_params)
    serializer = self.serializer_class[0](data=request.query_params)
    if not serializer.is_valid():
        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
    # 判断用户名是否存在；
    try:    
      # 获取用户信息
      user = User.objects.get(username=serializer.validated_data['username'])
    except User.DoesNotExist:
      return Response({"msg":"用户不存在"},status=HTTP_204_NO_CONTENT)
    
    # 用户存在，进行密码校验
    if not check_password(serializer.validated_data['username'],user.password):
        return Response({'msg':"用户名或密码输入错误"},status=HTTP_202_ACCEPTED)
    
    # 获取用户的 token
    import jwt,datetime,django_redis 
    salt = settings.SECRET_KEY
    # 构造Header，默认如下
    headers = {
        'typ':'jwt',
        'alg':'HS256'
    }
    # 构造Payload
    payload = {
        'id':user.id,#自定义用户ID
        'username':user.username,#自定义用户名
        'exp':datetime.datetime.utcnow()+datetime.timedelta(days=1),# 设置超时时间，7 天内
    }
    token = jwt.encode(headers=headers,payload=payload,key=salt,algorithm='HS256')
    redis_con = django_redis.get_redis_connection('default') 
    redis_con.set(token,user.username,60*60*24)
    return Response(data={
        "Id":user.id,
        "Username":user.username,
        "Token":token,
    },status=HTTP_200_OK)

@api_view(['POST'])
def AnyUserRegister(self,request,*args,**kwargs):
    ''' 注册 Any用户 '''
    import django_redis
    if kwargs['type'] == 'cell':
      ce
      #  手机注册
      serializer = CellRegistererializer(data=request.data)
      if not serializer.is_valid(raise_exception=True):
        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)  
      # 2. 检验 code 是否过期。
      cellphone = serializer.validated_data['cell']
      code = serializer.validated_data['code']
      # 获取 redis.conn 的 verify_code 中 key 为 code 的信息
      redis_con = django_redis.get_redis_connection('verify_code') 
      # 判断 手机验证码是否过期
      if redis_con.ttl(cellphone) == -2:
        return Response({'msg':'验证码已失效'},status=HTTP_400_BAD_REQUEST)

      # 3. 检验验证码是否匹配。
      if  redis_con.get(cellphone).decode() != code:
          return Response({'msg':'验证码错误'},status=HTTP_400_BAD_REQUEST)

      # 4. 检验完成创建用户
      try:
        serializer.create()
      except UserAlreadyExists:
          return Response({'msg':"用户已存在"},status=HTTP_400_BAD_REQUEST)
      headers = self.get_success_headers(serializer.data)
      print(headers)
      return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)
    elif kwargs['type'] == 'email':
      emailRegister(self,request)
    else:
       return Response(HTTP_404_NOT_FOUND)
    


    def emailRegister():
       print('email')


class AnyUserLoginRegister(APIView):
    
   queryset = User.objects.all()
   serializer_class = [LoginSerializer,EmailRegistererializer,CellRegistererializer] 
    

class AnyUserListCreate(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = [UserListSerializer,CreateSerializer] 

    def list(self,request, *args, **kwargs):
      queryset = self.get_queryset()
      total = queryset.count()
      serializer = self.serializer_class[0](queryset, many=True)
      return Response({'total':total,'list':serializer.data},status=HTTP_200_OK)

    def create(self, request, *args, **kwargs):
      """ 创建 Any用户 
      初始字段：
        password: 随机密码，方式 

      request.data:
        username:
        gender:
        cell:
        email:
        is_anonymous:
      """
      serializer = self.serializer_class[1](data=request.data)
      if not serializer.is_valid(raise_exception=True):
        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
      pw =serializer.create()
      return Response({**serializer.validated_data,**{'password':pw}}, status=HTTP_201_CREATED)
        
    def get_queryset(self):
      # uid = self.request.query_params.get('id', None)
      username = self.request.query_params.get('username', None)
      # gender = self.request.query_params.get('gender', None)
      # cell = self.request.query_params.get('cell', None)
      # active = self.request.query_params.get('active', None)
      # date_joined = self.request.query_params.get('date_joined', None)
      pageNum = self.request.query_params.get('pageNum', 1)
      pageSize = self.request.query_params.get('pageSize', 10)
      if not isinstance(pageNum,int) and pageNum>0 :
         return Response({'msg':'pageNum或pageSize错误！'},status=HTTP_400_BAD_REQUEST)
      
      if not isinstance(pageSize ,int) and (pageSize >0) and (pageSize % 10 == 0):
         return Response({'msg':'pageSize或pageNum错误！'},status=HTTP_400_BAD_REQUEST)
      queryset = self.queryset
      if username is not None:
         queryset=self.queryset.filter(username=username)
      return queryset[(pageNum-1)*pageSize:pageSize]


class AnyUserUpdateDelete(mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          GenericAPIView):
   
   def update(self, request, *args, **kwargs):



      return super().update(request, *args, **kwargs)
   

   
# class UserSearch(generics.ListAPIView):
#     queryset = User.objects.filter(is_staff=False)
#     serializer_class = UserListSerializer

#     def list(self,request,*args,**kwargs):
#       queryset = self.get_queryset()
#       total = queryset.count()
#       serializer = self.serializer_class(queryset, many=True)
#       return Response({'total':total,'list':serializer.data},status=HTTP_200_OK)



class AdminLogin(APIView):
    serializer_class = LoginSerializer 

    def get(self,request,*args,**kwargs):
      ''' Admin用户登录 
      username:
      password:
      return {'id':user.id,'username':user.username,'token':jwt_token}
      '''

      # 密码解密



      serializer = self.serializer_class(data=request.query_params)
      if not serializer.is_valid():
          return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)


      # 判断用户名是否存在；
      try:
          user = AdminUser.objects.get(username=serializer.validated_data['username'])
      except AdminUser.DoesNotExist:
        return Response({"msg":"用户不存在"},status=HTTP_400_BAD_REQUEST)  
      

      # 用户存在，进行密码校验
      if not check_password(serializer.validated_data['password'],user.password):
          return Response({'msg':"用户名或密码输入错误"},status=HTTP_400_BAD_REQUEST)
      

      # 获取用户的 toke
      salt = settings.SECRET_KEY
      # 构造Header，默认如下
      headers = {
          'typ':'jwt',
          'alg':'HS256'
      }
      # 构造Payload
      payload = {
          'id':user.id,#自定义用户ID
          'username':user.username,#自定义用户名
          'exp':datetime.datetime.utcnow()+datetime.timedelta(days=1),# 设置超时时间，7 天内
      }
      token = jwt.encode(headers=headers,payload=payload,key=salt,algorithm='HS256')
      redis_con = django_redis.get_redis_connection('default') 
      redis_con.set(token,user.username,60*60*24)

      return Response(data={
          "id":user.id,
          "username":user.username,
          "token":token,
      },status=HTTP_200_OK)


class UserInfoDelete(RetrieveDestroyAPIView):
   
    def retrieve(request, *args, **kwargs):
        ''' 获取用户信息 '''
        pass
    
    def destroy(request, *args, **kwargs):
        ''' 删除用户 '''
        pass
    
    def get_queryset(self):
      keywords = self.qrequest.query_params.get('keywords',None)
      status = self.qrequest.query_params.get('status',None)
      pageNum= self.qrequest.query_params.get('pageNum',None)
      pageSize=self.qrequest.query_params.get('pageSize',None)
      if keywords is not None:
          #  搜索关键词
          queryset1=self.queryset.filter(username=keywords)
          
          # queryset2=self.queryset.filter(cell=keywords)
          total = queryset1.count()
          return  Response({'total':total,'list':queryset1},status=HTTP_200_OK)
      return super().get_queryset(self)
    






@api_view(['Delete'])
def Logout(request,uid):
    ''' 用户注销 '''
    try:
      User.objects.get(id=uid).delete()
    except User.DoesNotExist:
        return Response(data={"msg":"用户不存在",},status=HTTP_400_BAD_REQUEST)
    return Response(data={"msg":"退出成功",},status=HTTP_200_OK)




@api_view(['GET'])
def Repetition(request,name):
    ''' 查询用户名是否已存在 '''
    try:
        User.objects.get(username=name)
    except User.MultipleObjectsReturned:
        return Response(data={"msg":"用户名已存在"},status=HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response(data={"msg":"用户名不存在"},status=HTTP_204_NO_CONTENT)
    return Response(data={"msg":"OK"},status=HTTP_200_OK)
        
class UserInfoCreateDelete(APIView):
    def get(self,request,uid):
        ''' 获取指定用户信息 '''
        user = User.objects.get(id=uid)
        avatarUrl = user.avatar.url
        active = user.is_active
        staff = user.is_staff
        t = user.date_joined.date()
        joined = '{0}-{1}-{2}'.format(t.year,t.month,t.day)
        data={
            "Username":user.username,
            "Avatar":avatarUrl,
            'Active':active,
            'Staff':staff,
            'joined':joined,
        }
        return Response(data=data,status=HTTP_200_OK)

    def post(self,request):
       ''' 创建用户 '''
       pass







