
from django.urls import path,include,re_path

from .views import (
    AnyUserLoginRegister,
    AdminLogin,
    Logout,
    Repetition,
    AnyUserListCreate,
    UserInfoCreateDelete,
    
    # UserSearch,
)

urlpatterns=[
    re_path(r'^anyuser$',AnyUserListCreate.as_view(),name='UserlistCreate'),


    re_path(r'^anyuser/login$',AnyUserLoginRegister.as_view(),name="anyuserlogin"),
    re_path(r'^adminuser/login$',AdminLogin.as_view(),name="adminlogin"),
    # re_path(r'^login$',Login,name="login"),
    # re_path(r'^$',UserSearch.as_view(),name="Search"),

    # re_path(r'^search$',UserListCreate.as_view(),name="QueryParams"),
    # re_path(r'^logout/<uid>',Logout,name="logout"), 
    # re_path(r'^repetition/<name>',Repetition,name='UserRepetition'), # 查询用户名是否重复
    # re_path(r'<uid>',UserInfoCreateDelete.as_view(),name='getUserInfo'), # 查询用户信息(avatar\active\staff\)
    # path('test',test,name="test"),

]