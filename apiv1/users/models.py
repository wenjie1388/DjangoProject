from django.db import models
from django.contrib.auth.models import UserManager,PermissionsMixin,AbstractBaseUser,AbstractUser as _AbstractUser
from django.contrib.auth.models import User
# from django.contrib.auth.hashers import (
#     check_password,
#     is_password_usable,
#     make_password,
# )
from django.conf import settings
from django.forms import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_204_NO_CONTENT,
)
from utils.utils import get_RandomString,get_RandomPassword,send_mail
from .utils import AnyUserManager,AdminUserManager

def user_img_path(instance, filename):
    return 'users/{0}/{1}{2}'.format(instance.course.id,get_RandomString(24), filename)

class UserBase(AbstractBaseUser):
    ''' 用户基表 '''
    MALE = [
        ('M','男'),
        ('F','女'),
    ]
    username = models.CharField(
        verbose_name='用户名',
        max_length=128,
        unique=True,
    )
    password = models.CharField(
        verbose_name='密码',
        max_length=128,
        help_text="6-20个字符、密码不能与用户名相同、^[a-zA-Z](?![a-zA-Z]{5,19}$)([a-zA-Z0-9_.@$!%*#_~?&^]{5,19}$)",
    )
    cellphone = models.CharField(
        verbose_name='手机号',
        max_length=128,
        blank=True,
        unique=True,
        null=True,
    )
    name = models.CharField(
        verbose_name='姓名',
        max_length=128,
        blank=True,
    )
    id_card = models.CharField(
        verbose_name='身份证件',
        max_length=128,
    )
    male = models.CharField( 
        verbose_name='性别',
        max_length=128,
        choices=MALE,
        help_text="M是男；F是女！",
        blank=True,
    )
    avatar = models.ImageField(
        verbose_name="头像",
        upload_to=user_img_path,
        default='users/default/default.jpg'
    )
    email = models.EmailField(
        verbose_name="邮箱",
        max_length=128,
        blank=True,
        unique=True,
        null=True,
    )
    address = models.CharField(
        verbose_name="居住地",
        max_length=128,
        blank=True,
    )
    date_joined = models.DateField(
        verbose_name="注册时间",
        auto_now_add=True,
    )
    
    is_authenticated=models.BooleanField(
        verbose_name="是否已认证",
        default=False,
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
      abstract = True
    
    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return False
    
    def get_jwt_auth(self):
        return ''
    

    # def set_password(self, raw_password):
    #     self.password = make_password(raw_password)
    #     self._password = raw_password

    def check_password(self, raw_password):
        if self.password != raw_password:
          # raise ValidationError(self.errors)
          return False
        return True
        
        
        
    def email_user(self, subject, message,to_email ,from_email=settings.EMAIL_HOST_USER, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [to_email], **kwargs)

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)


class Admin(UserBase):
    DEPARTMENT = [
        ('D','开发部门'),
        ('A','审核部门'),
    ]
    STATE=[
        ('S','病假'),
        ('P','事假'),
        ('A','年假'),
    ]

    department=models.CharField(
        '部门',
        max_length=1,
        choices=DEPARTMENT,
    )
    state=models.CharField(
        '状态',
        max_length=1,
        choices=STATE,
    )
    is_superuser = models.BooleanField(
        '是否是超级管理员',
        default=False,
    )
    
    objects = AdminUserManager()
    REQUIRED_FIELDS = ["email"]
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    class Meta:
        db_table = 'admin'
        ordering = ('id',)
        verbose_name = 'admin'
        verbose_name_plural = 'admins'

class User(UserBase):
    ''' User 表 '''
    introduction = models.TextField(
        verbose_name="个性签名",
        max_length=200,
        blank=True,
    )
    
    is_activate = models.BooleanField(
        verbose_name="是否已激活",
        default=True,
    )
    objects = AnyUserManager()
    class Meta:
        db_table = 'user'
        ordering = ('id','date_joined')
        verbose_name = 'user'
        verbose_name_plural = 'users'




'''
class SMSCode(models.Model):
    #  手机验证码表 
    mobile = models.CharField(
        max_length=11,
        help_text='手机号',
    )
    code = models.CharField(
        max_length=6,
        help_text='验证码',
    )
    isExpires = models.BooleanField(
        default= False,
        help_text='是否失效'
    )
    createDate = models.DateTimeField(
        auto_now_add=True,
        help_text='创建日期'
    )
    expiresDate = models.DateTimeField(
        default=now()+timedelta(minutes=10),
        help_text='失效时间'
    )

class LogRegister(models.Model):
    username = models.CharField(
        max_length=20,
        unique=True,
        help_text="Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[UsernameValidator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    password = models.CharField("password", max_length=128)
    createDate = models.DateField(auto_now_add=True)
    expiresDate= models.DateTimeField(default=now()+timedelta(minutes=30))

'''



