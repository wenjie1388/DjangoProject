
from django.urls import path,include,re_path
from rest_framework import routers
from .views import (
    UserLoginView,
    UserViewset,
    AnyUserLoginView,
    AnyUserRegisterView,
    AnyUserListCreateView,
    
    AdminUserLoginView,
    AdminUserView,

)



urlpatterns=[
    # AnyUser接口
    re_path(
        r'^login$',
        UserLoginView.as_view(),
        name="userLogin"
    ),

    # re_path(r'',include(router.urls)),
    re_path(r'^anyuser/login$',AnyUserLoginView,name="anyuserLogin"),
    re_path(r'^anyuser/register$',AnyUserRegisterView,name="anyuserRegister"),
    # re_path(r'^anyuser/(?P<id>.+)/$',AnyUserViewset.as_view({"get":""}),name="anyUserViewset"),

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


router = routers.SimpleRouter()
router.register(r'', UserViewset)
urlpatterns += router.urls
