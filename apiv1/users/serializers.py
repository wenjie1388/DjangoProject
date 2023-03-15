from rest_framework import serializers
from django.utils.translation import gettext as _
from django.core.validators import BaseValidator
from django.core.validators import (RegexValidator)

from .models import AnyUser as User

from .utils import UsernameField,PasswordField,CellphoneField,RandomStringField_6
from .exceptions import UserAlreadyExists

from utils.utils import get_RandomPassword



''' 以下是序列器：登录序列器 、 用户注册序列器'''
class LoginSerializer(serializers.Serializer):
    username = UsernameField()
    password = PasswordField()

class CreateSerializer(serializers.Serializer):
    
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
        # if User.objects.filter(username=self.validated_data['username']) == []:
        #     raise UserAlreadyExists
        # pw = self.set_password()
        # User.objects.create(
        #     username=self.validated_data['username'],
        #     password=pw,
        #     cell=self.validated_data['cell'],
        # )
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
        
    

class RegisterSerializer(serializers.Serializer):
    pass

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('address','avatar','idcard','name','introduction')
        # 将exclude属性设置成一个从序列化器中排除的字段列表。
        # 但是你也可以使用depth选项轻松生成嵌套关联：
        # fields = ('id','username','cell','gender','name','idcard','email','is_active','last_login','date_joined')




