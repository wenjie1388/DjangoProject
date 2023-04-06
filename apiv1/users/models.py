from django.db import models
from django.contrib.auth.models import UserManager,PermissionsMixin,AbstractBaseUser,AbstractUser as _AbstractUser
from django.contrib.auth.hashers import (
    check_password,
    is_password_usable,
    make_password,
)
from django.conf import settings

from utils.utils import get_RandomString,get_RandomPassword

def user_img_path(instance, filename):
    return 'users/{0}/{1}{2}'.format(instance.course.id,get_RandomString(24), filename)

class UserBase(models.Model):
    ''' 用户基表 '''
    GENDER = [
        ('M','男'),
        ('F','女'),
    ]
    username = models.CharField(
        verbose_name='用户名',
        max_length=50,
        unique=True,
    )
    password = models.CharField(
        verbose_name='密码',
        max_length=128,
        help_text="6-20个字符、密码不能与用户名相同、^[a-zA-Z](?![a-zA-Z]{5,19}$)([a-zA-Z0-9_.@$!%*#_~?&^]{5,19}$)",
    )
    cell = models.CharField(
        verbose_name='手机号',
        max_length=11,
    )
    name = models.CharField(
        verbose_name='姓名',
        max_length=10,
    )
    idcard = models.CharField(
        verbose_name='身份证件',
        max_length=18,
    )
    gender = models.CharField( 
        verbose_name='性别',
        max_length=1,
        choices=GENDER,
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
        blank=True,
    )
    address = models.CharField(
        verbose_name="居住地",
        max_length=50,
        blank=True,
    )
    date_joined = models.DateField(
        verbose_name="注册时间",
        auto_now_add=True,
    )
    is_anonymous = models.BooleanField(
        verbose_name="是否已激活",
        default=False,
    )
    is_authenticated=models.BooleanField(
        verbose_name="是否已认证",
        default=False,
    )
    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.username
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])

        return check_password(raw_password, self.password, setter)
    
    @staticmethod
    def get_initial_password():
        ''' 返回24位初始密码 '''
        return get_RandomPassword(24)



    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        print(subject, message, from_email, [self.email], **kwargs)
        raise "已经打印"

    
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
 



class AdminUser(UserBase,PermissionsMixin):
    from .utils import AdminUserManager
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
        verbose_name = ('admin')
        verbose_name_plural = ('admins')

    

class AnyUser(UserBase):
    ''' User 表 '''
    introduction = models.TextField(
        verbose_name="个性签名",
        max_length=200,
        blank=True,
    )
    

    class Meta:
        db_table = 'user'
        ordering = ('id',)
        verbose_name = ('user')
        verbose_name_plural = ('users')

    
    



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



