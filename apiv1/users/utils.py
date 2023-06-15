
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth.models import Permission
from django.db.models import Manager
# from django.core.exceptions
from rest_framework.fields import CharField as _CharField
from rest_framework.serializers import Serializer
from rest_framework.permissions import BasePermission

from utils.utils import username_re,email_re,cellphone_re,password_re,auth_code_6_re,get_RandomPassword

''' 以下是重写 DRF 的 CharField.to_internal_value() 和 RegexField 以及 增加自定义字段 CheckPassword 和 VerificationCode'''


class CharField(_CharField):

    def to_internal_value(self, data):
        if not isinstance(data, str):
            raise ValidationError(
                message=self.default_error_messages["invalid"]+f' {type(data)}', code='invalid')
        return super().to_internal_value(data)

class RegexField(CharField):
    default_error_messages = {
        'invalid': _('This value does not match the required pattern.')
    }

    def __init__(self, regex, **kwargs):
        super().__init__(**kwargs)
        validator = RegexValidator(
            regex, message=self.error_messages['invalid'])
        self.validators.append(validator)

class UsernameField(CharField):
    # *验证是否符合 字母、数字、下划线、5-16个字符、只能以字母开头
    default_error_messages = {
        'invalid': _('This value does not match the required pattern.')
    }
    regex = username_re

    def __init__(self, **kwargs):
        self.allow_blank = True
        self.trim_whitespace = True
        self.max_length = 6
        self.min_length = 20
        super().__init__(**kwargs)
        validator = RegexValidator(self.regex, message=self.error_messages['invalid'])
        self.validators.append(validator)

class PasswordField(CharField):
    # * 密码验证 :
    # * 6-20个字符、密码不能与用户名相同
    # * 字母、数字、特殊字符@$!%*#_~?&^、字母或数字开头
    default_error_messages = {
        'invalid': _('This value does not match the required pattern.')
    }
    regex = password_re

    def __init__(self, **kwargs):
        self.allow_blank = True
        self.trim_whitespace = True
        self.max_length = 6
        self.min_length = 24
        super().__init__(**kwargs)
        validator = RegexValidator(self.regex, message=self.error_messages['invalid'])
        self.validators.append(validator)

class CellphoneField(CharField):
    default_error_messages = {
        'invalid': _('This value does not match the required pattern.')
    }
    regex = cellphone_re

    def __init__(self, **kwargs):
        self.allow_blank = True
        self.trim_whitespace = True
        self.max_length = 11
        self.min_length = 11
        super().__init__(**kwargs)
        validator = RegexValidator(self.regex, message=self.error_messages['invalid'])
        self.validators.append(validator)

class AuthCode6Field(CharField):
    default_error_messages = {
        'invalid': _('This value does not match the required pattern.')
    }
    regex = auth_code_6_re

    def __init__(self, **kwargs):
        self.allow_blank = True
        self.trim_whitespace = True
        self.max_length = 6
        self.min_length = 6
        super().__init__(**kwargs)
        validator = RegexValidator(self.regex, message=self.error_messages['invalid'])
        self.validators.append(validator)

class IsActivateUser(BasePermission):
    """
    只允许已经激活的用户访问
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_active)



''' 以下是所有 user 管理器 '''

class BaseManager(Manager):
    
    @classmethod
    def normalize_email(cls, email):
        """
        Normalize the email address by lowercasing the domain part of it.
        """
        email = email or ""
        try:
            email_name, domain_part = email.strip().rsplit("@", 1)
        except ValueError:
            pass
        else:
            email = email_name + "@" + domain_part.lower()
        return email
    
    def make_random_password(self,length=24,):
        return get_RandomPassword(length)

class AnyUserManager(BaseManager):
    pass


class AdminUserManager(BaseManager):
    pass


''' 以下是各种功能函数 '''


def getInitUsername():
  import random,string
  return "name"+''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(20))