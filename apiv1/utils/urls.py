
from django.urls import path,include,re_path

from .views import (
    CaptchaViews
)

urlpatterns=[
    # re_path(r"sms/(?P<cell>.*)",SMSCodeView,name="SMSCode"),
    re_path(r"captcha",CaptchaViews.as_view(),name="captcha"),
    
]