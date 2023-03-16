
from django.apps import apps
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.base_user import  BaseUserManager
from django.contrib.auth.hashers import make_password
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext as _
from django.db import models
# from django.core.exceptions
from rest_framework.fields import CharField as _CharField
from rest_framework.serializers import Serializer
from rest_framework.permissions import BasePermission

from utils.utils import username_re,email_re,cellphone_re,password_re,randomStr6_re


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

class RandomStringField_6(CharField):
    default_error_messages = {
        'invalid': _('This value does not match the required pattern.')
    }
    regex = randomStr6_re

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



''' 以下是 user管理器 '''
class AnyUserManager(BaseUserManager):
    pass

class AdminUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_anonymous", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_anonymous", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_anonymous") is not True:
            raise ValueError("Superuser must have is_anonymous=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)