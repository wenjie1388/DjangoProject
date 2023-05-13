from rest_framework import serializers

from django.utils.translation import gettext as _
from django.core.validators import BaseValidator,RegexValidator

from django.db import IntegrityError
from django.contrib.auth.hashers import (
    check_password,
    is_password_usable,
    make_password,
)
from .models import AnyUser as User,AdminUser

from .utils import UsernameField,PasswordField,CellphoneField,AuthCode6Field
from .exceptions import UserAlreadyExists

from auth.utils import get_RandomPassword,get_RandomString


''' 以下是基类序列器 '''

class LoginBaseSerializer(serializers.Serializer):
    password = PasswordField()

class RegisterBaseSerializer(serializers.Serializer):
    ''' 注册基类 '''
    password = PasswordField()
    code = AuthCode6Field()

    def create(self):
      email=self.validated_data.get("email",None)
      cell=self.validated_data.get("cell",None)
      pw=self.validated_data.get("password",None)
      username=get_RandomString(24)
      
      if email is not None:
        # 邮箱注册
        user_info = {"username":username,"password":pw,"email":email}

      elif cell is not None:
        # 手机号码注册
        user_info = {"username":username,"password":pw,"cell":cell}
      else:
          return 0
      
      try:
        User.objects.create(**user_info)
      except IntegrityError:
          return 0
      return user_info


''' 以下是AnyUser模型的序列器 '''

class AnyUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('address','avatar','idcard','name','introduction')
        # 将exclude属性设置成一个从序列化器中排除的字段列表。
        # 但是你也可以使用depth选项轻松生成嵌套关联：
        # fields = ('__all__')

class AnyUserLoginEmailSerializer(LoginBaseSerializer):
    email = serializers.EmailField()

class AnyUserLoginUsernameSerializer(LoginBaseSerializer):
    username = UsernameField()

class AnyUserLoginCellSerializer(LoginBaseSerializer):
    cell = CellphoneField()

class AnyUserRegisterEmailSerializer(RegisterBaseSerializer):
    ''' 邮箱注册序列器 '''
    email=serializers.EmailField()

class AnyUserRegisterCellSerializer(RegisterBaseSerializer):
    ''' 手机号注册序列器 '''
    cell = CellphoneField()

class AnyUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('address','avatar','idcard','name','introduction')
        # 将exclude属性设置成一个从序列化器中排除的字段列表。
        # 但是你也可以使用depth选项轻松生成嵌套关联：
        # fields = ('id','username','cell','gender','name','idcard','email','is_active','last_login','date_joined')

class AnyUserCreateSerializer(serializers.Serializer):
    ''' 添加用户序列器 '''
    GENDER = [
        ('M','男'),
        ('F','女'),
    ]
    email=serializers.EmailField()
    is_anonymous=serializers.BooleanField()
    username = UsernameField()
    cell = CellphoneField()
    gender=serializers.ChoiceField(
        choices=GENDER
        )


    def create(self, **kwargs):
        if self.validated_data.get('password',None):
            User.objects.create(**self.validated_data)
        else:
            pw = self.get_initial_password()
            User.objects.create(**self.validated_data,**{"password":pw})
            return pw
        return User
    
    def get_initial_password(self):
        ''' 返回初始密码 '''
        return get_RandomPassword(24)




''' 以下是AdminUser模型的序列器 '''

class AdminUserLoginSerializer(LoginBaseSerializer):
    pass

class AdminUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        # exclude = ('address','avatar')
        # 将exclude属性设置成一个从序列化器中排除的字段列表。
        # 但是你也可以使用depth选项轻松生成嵌套关联：
        # fields = ('id','username','cell','gender','name','idcard','email','is_active','last_login','date_joined')
    
class AdminUserCreateSerializer(serializers.Serializer):
    ''' 添加管理员 序列器'''
    username = UsernameField()
    email = serializers.EmailField()
    
    def create(self,validated_data):
        return AdminUser.objects.create(**validated_data)
    
class AdminUserModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AdminUser
        exclude = ('address','avatar')



