
from django.urls import path,include,re_path
from rest_framework.routers import DefaultRouter
from .views import (
    AnyUserViewset,
    AnyUserLoginView,
    AnyUserRegisterView,
    AnyUserListCreateView,
    
    AdminUserLoginView,
    AdminUserView,

)

urlpatterns=[
    # AnyUser接口

    # re_path(r'^anyuser/(?P<id>.+)/$',AnyUserLoginView,name="anyuserlogin"),
    re_path(r'^anyuser/login$',AnyUserLoginView,name="anyuserLogin"),
    path('anyuser/register/<type>',AnyUserRegisterView,name="anyuserRegister"),
  
    # ''' AdminUser接口 '''
    re_path(r'^adminuser$',AdminUserView.as_view(),name="AdminUser"),
    re_path(r'^adminuser/(?P<id>.+)/$',AdminUserView.as_view(),name="AdminUser"),
    re_path(r'^adminuser/login$',AdminUserLoginView.as_view(),name="adminlogin"),
    # re_path(r'^adminuser/:$',AdminUserLoginView.as_view(),name="adminlogin"),
    # re_path(r'^login$',Login,name="login"),
    # re_path(r'^$',UserSearch.as_view(),name="Search"),

    # re_path(r'^search$',UserListCreate.as_view(),name="QueryParams"),
    # re_path(r'^logout/<uid>',Logout,name="logout"), 
    # re_path(r'^repetition/<name>',Repetition,name='UserRepetition'), # 查询用户名是否重复
    # re_path(r'<uid>',UserInfoCreateDelete.as_view(),name='getUserInfo'), # 查询用户信息(avatar\active\staff\)
    # path('test',AdminTestList.as_view(),name="test"),
]

router = DefaultRouter()
router.register('anyuser',AnyUserViewset)

urlpatterns += router.urls