from django.contrib.auth import views

from django.conf import settings
from django.core.cache import cache
from django.contrib.auth.hashers import check_password,make_password
from django.db.utils import IntegrityError

from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.utils.translation import gettext as _

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,RetrieveDestroyAPIView
from rest_framework.status import (
    HTTP_200_OK,HTTP_201_CREATED,HTTP_202_ACCEPTED,HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,HTTP_401_UNAUTHORIZED,HTTP_404_NOT_FOUND,HTTP_405_METHOD_NOT_ALLOWED,HTTP_406_NOT_ACCEPTABLE,
    HTTP_500_INTERNAL_SERVER_ERROR
)
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.settings import api_settings
from rest_framework import authentication, permissions,mixins
from rest_framework.generics import  ListAPIView,ListCreateAPIView
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

import jwt,datetime,django_redis 
from .models import AnyUser as User,AdminUser
from .serializers import (
   AnyUserLoginUsernameSerializer,
   AnyUserLoginCellSerializer,
   AnyUserLoginEmailSerializer,
   AnyUserModelSerializer,
   AnyUserCreateSerializer,
   AnyUserListSerializer,
   AnyUserRegisterCellSerializer,
   AnyUserRegisterEmailSerializer,
  
   AdminUserModelSerializer,
   AdminUserLoginSerializer,
   AdminUserListSerializer,
   AdminUserCreateSerializer,
   AdminUserLoginSerializer,
   )
from .exceptions import UserAlreadyExists
from auth.crypto import CryptoAES
from auth.utils import JwtToken,send_mail




''' 以下是AnyUser的接口 '''

@api_view(['GET'])
def AnyUserLoginView(request):
    ''' Any用户登录 '''
    # 获取请求数据，判断登录方式。若无用户信息，则进行注册
    req_params = request.query_params.dict()
    try:
      method = req_params.pop("method")
    except KeyError:
       return Response({'msg':f'{method} 方法不存在'},status=HTTP_400_BAD_REQUEST)
    if method == "username":
        serializer = AnyUserLoginUsernameSerializer(data=req_params)
        serializer.is_valid(raise_exception=True)
        try:
          # 获取用户信息
          username = serializer.validated_data['username']
          user = User.objects.get(username=username)
        except User.DoesNotExist:
          return Response({"msg":f"账户：{username} 不存在。"},status=HTTP_400_BAD_REQUEST)
    elif method == "cell":
        serializer = AnyUserLoginCellSerializer(data=req_params)
        serializer.is_valid(raise_exception=True)
        try:
          # 获取用户信息
          cell = serializer.validated_data['cell']
          user = User.objects.get(cell=cell)
        except User.DoesNotExist:
          return Response({"msg":f"手机号：{cell} 不存在。"},status=HTTP_400_BAD_REQUEST) 
        

    elif method == "email":
        serializer = AnyUserLoginEmailSerializer(data=req_params)
        serializer.is_valid(raise_exception=True)
        try:
          # 获取用户信息
          email = serializer.validated_data['email']
          user = User.objects.get(email=email)
        except User.DoesNotExist:
          return Response({"msg":f"邮箱：{email} 不存在。"},status=HTTP_400_BAD_REQUEST)        
        except User.MultipleObjectsReturned:
          return Response({"msg":f"邮箱：{email} 重复存在。"},status=HTTP_400_BAD_REQUEST)
    else:
        return Response({"method": f" {method} 方式不被允许。"},status=HTTP_400_BAD_REQUEST)
    
    if user.is_activate == False:
       return Response({"mgs":["此账号未激活"]},status=HTTP_400_BAD_REQUEST)

    # 用户存在，进行密码校验
    # if not check_password(serializer.validated_data['password'],user.password):
    _password = serializer.validated_data['password']
    password = user.password
    if _password !=password :
        return Response({'msg':"用户名或密码输入错误"},status=HTTP_400_BAD_REQUEST)

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
def AnyUserRegisterView(request):
    ''' 注册 Any用户 '''
    import django_redis

    req_data = request.data
    method = request.query_params.get("method",None)
    if method is None:
       return Response({'msg':['缺少 method 参数']},status=HTTP_400_BAD_REQUEST)

    if method == 'cell':
      #  手机注册
      serializer = AnyUserRegisterCellSerializer(data=req_data)
      serializer.is_valid(raise_exception=True)

    elif method == 'email':
      #  邮箱注册
      serializer = AnyUserRegisterEmailSerializer(data=req_data)
      serializer.is_valid(raise_exception=True)

    else:
       return Response({"msg":["method 参数错误，只能是 'Cell' 或 'Email'."]},HTTP_400_BAD_REQUEST)

    verify_code = serializer.validated_data['code']
    # 获取 redis.conn 的 verify_code 中 key 为 code 的信息
    redis_con = django_redis.get_redis_connection('verify_code') 
    verify_method = serializer.validated_data[method]
    # 2. 检验 verify_filter 是否过期。
    if redis_con.ttl(verify_method) == -2:
      return Response({'msg':['验证码错误或已失效']},status=HTTP_400_BAD_REQUEST)

    # 3. 检验验证码是否匹配。
    if  redis_con.get(verify_method).decode() != verify_code:
        return Response({'msg':['验证码错误']},status=HTTP_400_BAD_REQUEST)
    
    # 4. 检验完成创建用户
    user_info = serializer.create()
    if not user_info:
      return Response({'msg':["用户已存在"]},status=HTTP_400_BAD_REQUEST)
    return Response(status=HTTP_201_CREATED)




class AnyUserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AnyUserModelSerializer
    lookup_field = "id"

class AnyUserListCreateView():

    queryset = User.objects.all()
    serializer_class = [AnyUserListSerializer,AnyUserCreateSerializer] 

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

class AnyUserUpdateDeleteView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView
    ):
   
    lookup_field = 'id'

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['username']
        return User.objects.filter(user__username=username)


''' 以下是AdminUser模型的接口 '''

class AdminUserLoginView(APIView):
    
    def get(self,request):
      ''' Admin登录 
      username:
      password:
      return {'id':user.id,'username':user.username,'token':jwt_token}
      '''
      serializer_class = AdminUserLoginSerializer

      serializer = serializer_class(data=request.query_params)
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

      # 获取 JWT
      token=JwtToken.get_HS256({
          'id':user.id,#自定义用户ID
          'username':user.username,#自定义用户名
          'exp':datetime.datetime.utcnow()+datetime.timedelta(days=1),# 设置超时时间，7 天内
      })

      # 连接 redis 存JWT
      redis_con = django_redis.get_redis_connection('default') 
      redis_con.set(token,user.username,60*60*24)
      return Response(data={
          "id":user.id,
          "username":user.username,
          "token":token,
      },status=HTTP_200_OK)

class AdminUserView(APIView):
    '''  用户列表|新增 AdminUser  '''
    queryset = AdminUser.objects.all()
    serializer_class = [AdminUserListSerializer,AdminUserCreateSerializer]

    def get(self,request, *args, **kwargs):
      queryset = self.get_queryset()
      total = queryset.count()
      serializer = self.serializer_class[0](queryset, many=True)
      return Response({'total':total,'list':serializer.data},status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
      """ 添加 AdminUser 记录
      request.data:
        username:

      初始字段：
        password: 随机密码，方式 
      """
      serializer = self.serializer_class[1](data=request.data)
      if not serializer.is_valid(raise_exception=True):
        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
      total = AdminUser.objects.filter(username=serializer.validated_data['username']).count()
      if total > 0:
         return Response({_('message'):_('User already exists')},status=HTTP_400_BAD_REQUEST)
      pw = AdminUser.get_initial_password()
      user_dict = {**serializer.validated_data,**{'password':pw}}
      adminuser_obj = serializer.create(user_dict)
      serializer = AdminUserListSerializer(adminuser_obj,many=False)
      # if not send_mail(adminuser_obj):
      #    adminuser_obj.delete()
      #    return Response({'msg':'邮箱发送失败'},status=HTTP_400_BAD_REQUEST)
      return Response(serializer.data, status=HTTP_201_CREATED)

class PurchaseList(ListAPIView):
    serializer_class = AdminUserModelSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['id']
        # return User.objects.filter(purchaser__username=username)
    

    ''' 检索|更新|删除 AdminUser'''
    # queryset = AdminUser.objects.all()
    # serializer_class = AdminUserListSerializer 


   


''' ...... '''
@api_view(['Delete'])
def Logout(request,uid):
    ''' 用户注销 '''
    try:
      User.objects.get(id=uid).delete()
    except User.DoesNotExist:
        return Response(data={"msg":"用户不存在",},status=HTTP_400_BAD_REQUEST)
    return Response(data={"msg":"退出成功",},status=HTTP_200_OK)


@api_view(['GET'])
@authentication_classes((BasicAuthentication,))
@permission_classes((IsAuthenticated,))
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







