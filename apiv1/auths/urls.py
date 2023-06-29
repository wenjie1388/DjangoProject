
from django.urls import path,include,re_path
from rest_framework import routers
from .views import (
  CaptchaView
)


urlpatterns=[
  path('captcha/',CaptchaView.as_view(),name='captcha'),

]
