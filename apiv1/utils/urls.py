
from django.urls import path,include,re_path

from .views import (
    # CaptchaViews
    SMSCodeView,
    EmailCodeView,
    CaptchaView
)

urlpatterns=[
    # re_path(r"sms/(?P<cell>.*)",SMSCodeView,name="SMSCode"),
    # re_path(r"captcha",CaptchaViews.as_view(),name="captcha"),
    re_path(r"SMScaptcha",SMSCodeView,name="captcha"),
    re_path(r"Emailcaptcha",EmailCodeView,name="captcha"),
    
    re_path(r"captcha$",CaptchaView.as_view(),name="EmailCode"),
]