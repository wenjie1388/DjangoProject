
from django.urls import path,include,re_path

from .views import SMSCodeView

urlpatterns=[
    # re_path(r"sms/(?P<cell>.*)",SMSCodeView,name="SMSCode"),
    re_path(r"smscode",SMSCodeView,name="SMSCode"),
]