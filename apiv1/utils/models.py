from django.db import models
import binascii
import os

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User
import uuid
import jwt


class TokenBase(models.Model):
    
  class Meta:
    abstract = True
    
  def save(self, *args, **kwargs):
    if not self.key:
        self.key = self.generate_key()
    return super().save(*args, **kwargs)

  @classmethod
  def generate_key(cls,):
    return binascii.hexlify(os.urandom(20)).decode()

  def __str__(self):
      return self.key
    

class Token(TokenBase):
    """
    The default authorization token model.
    """
    key = models.CharField(_("Key"), max_length=255, primary_key=True)
    user = models.OneToOneField(
        User, related_name='+',
        on_delete=models.CASCADE, 
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        db_table = 'usertoken'
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")
    
    def generate_key2(headers,payload):
      return jwt.encode(payload=payload,key=settings.SECRET_KEY,headers=headers)

class AdminToken(TokenBase):
    """
    The default authorization admin_token model.
    """
    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='+',
        on_delete=models.CASCADE, verbose_name=_("admin")
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        # Work around for a bug in Django:
        # https://code.djangoproject.com/ticket/19422
        #
        # Also see corresponding ticket:
        # https://github.com/encode/django-rest-framework/issues/705
        db_table = 'admintoken'
        verbose_name = _("AdminToken")
        verbose_name_plural = _("AdminTokens")








"""
os.urandom  以字节方式生成随机加密字符串
binascii模块也在python的标准库中，hexlify就是十六进制化的意思。据python官方说，binascii模块比较底层，但是速度很快，效果跟bytes.hex一样。


"""