from rest_framework import serializers

from django.utils.translation import gettext as _
from django.core.validators import BaseValidator,RegexValidator

from django.db import IntegrityError
from django.contrib.auth.hashers import (
    check_password,
    is_password_usable,
    make_password,
)
from .models import User,Admin

from apiv1.filter import UsernameField,PasswordField,CellphoneField,AuthCode6Field,Captcha6Field,AccountField
from .exceptions import UserAlreadyExists

from utils.utils import get_RandomPassword,get_RandomString


''' 登录反序列器 '''

class LoginBaseSerializer(serializers.Serializer):
  password = PasswordField()

class CellphoneLoginSerializer(LoginBaseSerializer):
  account = CellphoneField()

class EmailLoginSerializer(LoginBaseSerializer):
  account = serializers.EmailField()

class UsernameLoginSerializer(LoginBaseSerializer):
  account = UsernameField()




class UserLoginSerializer(serializers.Serializer):
  account = AccountField()
  password = PasswordField()




class UserRegisterSerializer(serializers.Serializer):
  account = AccountField()
  password = PasswordField()
  
  def get_initial_password(self):
    ''' 返回随机密码 '''
    return get_RandomPassword(24)
  
  def save(self):
    import re
    validated_data={
      'username': 'email_'+self.validated_data['account']  if re.search('@',self.validated_data['account']) else 'phone_'+self.validated_data['account'],
      "email" if re.search('@',self.validated_data['account']) else "cellphone":self.validated_data['account'],
      "password":self.validated_data['password']
    }
 
    return User.objects.create(**validated_data)



class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # exclude = ('address','avatar','idcard','name','introduction')
        # 将exclude属性设置成一个从序列化器中排除的字段列表。
        # 但是你也可以使用depth选项轻松生成嵌套关联：
        fields = ('__all__')
    
    def save(self, **kwargs):
      assert hasattr(self, '_errors'), (
          'You must call `.is_valid()` before calling `.save()`.'
      )

      assert not self.errors, (
          'You cannot call `.save()` on a serializer with invalid data.'
      )

      # Guard against incorrect use of `serializer.save(commit=False)`
      assert 'commit' not in kwargs, (
          "'commit' is not a valid keyword argument to the 'save()' method. "
          "If you need to access data before committing to the database then "
          "inspect 'serializer.validated_data' instead. "
          "You can also pass additional keyword arguments to 'save()' if you "
          "need to set extra attributes on the saved model instance. "
          "For example: 'serializer.save(owner=request.user)'.'"
      )

      assert not hasattr(self, '_data'), (
          "You cannot call `.save()` after accessing `serializer.data`."
          "If you need to access data before committing to the database then "
          "inspect 'serializer.validated_data' instead. "
      )

      validated_data = {**self.validated_data, **kwargs}

      if self.instance is not None:
          self.instance = self.update(self.instance, validated_data)
          assert self.instance is not None, (
              '`update()` did not return an object instance.'
          )
      else:
          self.instance = self.create(validated_data)
          assert self.instance is not None, (
              '`create()` did not return an object instance.'
          )

      return self.instance
    

class AnyUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('address','avatar','idcard','name','introduction')
        # 将exclude属性设置成一个从序列化器中排除的字段列表。
        # 但是你也可以使用depth选项轻松生成嵌套关联：
        # fields = ('id','username','cellphone','gender','name','idcard','email','is_active','last_login','date_joined')

class AnyUserCreateSerializer(serializers.Serializer):
    ''' 添加用户序列器 '''
    GENDER = [
        ('M','男'),
        ('F','女'),
    ]
    email=serializers.EmailField()
    is_anonymous=serializers.BooleanField()
    username = UsernameField()
    cellphone = CellphoneField()
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
    





''' 以下是AdminUser模型的序列器 '''

class AdminUserLoginSerializer(LoginBaseSerializer):
    pass

class AdminUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        # exclude = ('address','avatar')
        # 将exclude属性设置成一个从序列化器中排除的字段列表。
        # 但是你也可以使用depth选项轻松生成嵌套关联：
        # fields = ('id','username','cellphone','gender','name','idcard','email','is_active','last_login','date_joined')
    
class AdminUserCreateSerializer(serializers.Serializer):
    ''' 添加管理员 序列器'''
    username = UsernameField()
    email = serializers.EmailField()
    
    def create(self,validated_data):
        return Admin.objects.create(**validated_data)
    
class AdminUserModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Admin
        exclude = ('address','avatar')



class AnyuserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



