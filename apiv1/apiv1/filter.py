from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth.models import Permission
from django.db.models import Manager
# from django.core.exceptions
from rest_framework.fields import CharField as _CharField
from rest_framework.serializers import Serializer
from rest_framework.permissions import BasePermission

username_re = r'^[a-zA-Z\u4e00-\u9fa5](?![0-9]+$)(?![a-zA-Z]+$)([a-z-A-Z0-9\u4e00-\u9fa5]{5,23}$)'# password_re=r'^[a-zA-Z0-9][a-zA-Z_0-9@$!%*#~?&^]{5,19}$'
password_re=r'^[a-zA-Z](?![0-9]+$)(?![a-zA-Z]+$)(?![a-zA-Z0-9]+$)([a-z-A-Z0-9,._]{5,23}$)'
cellphone_re = r'^1[3-9][0-9]{9}$'
# email_regex = r'^[\w]+@[\w]+.com$'
email_re = r'\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}'
auth_code_6_re=r'(?![a-zA-Z]{6})(?![0-9]{6})(^[a-zA-Z][0-9][a-zA-Z][0-9][a-zA-Z][0-9]$)'
captcha6_re = r'[0-9]{6}'
smscode_re= r'^(?![0-9]+$)(?![a-zA-Z]+$)([a-z-A-Z0-9]{6}$)'
gender_re = r'^[MF]{1}$'
account_re = f'({email_re})|({cellphone_re})'



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
        self.allow_blank = False
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
        self.allow_blank = False
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

class Captcha6Field(CharField):

    default_error_messages = {
        'invalid': _('This value does not match the required pattern.')
    }
    regex = captcha6_re

    def __init__(self, **kwargs):
        self.allow_blank = False
        self.trim_whitespace = True
        self.max_length = 6
        self.min_length = 6
        super().__init__(**kwargs)
        validator = RegexValidator(self.regex, message=self.error_messages['invalid'])
        self.validators.append(validator)

class AccountField(CharField):

    default_error_messages = {
        'invalid': _('This value does not match the required pattern.')
    }
    regex = account_re

    def __init__(self, **kwargs):
        self.allow_blank = False
        self.trim_whitespace = True
        self.max_length = 24
        self.min_length = 24
        super().__init__(**kwargs)
        validator = RegexValidator(self.regex, message=self.error_messages['invalid'])
        self.validators.append(validator)










        