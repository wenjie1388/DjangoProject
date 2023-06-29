
from django.urls import path,include,re_path
from rest_framework import routers
from .views import (
    UserLoginView,
    UserViewset,

)


urlpatterns=[
    # AnyUser接口
    re_path(
        r'^login/$',
        UserLoginView.as_view(),
        name="userLogin"
    ),
    path('',UserViewset.as_view({"get":"list","post":"create"})),
    re_path(r'^(?P<id>.+)/$',UserViewset.as_view({"get":"retrieve","update":"update","delete":"destroy"})),

]
