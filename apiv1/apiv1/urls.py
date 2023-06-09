# from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve
from django.conf import settings

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken import views

# from apiv1.settings import dev


urlpatterns = [
    re_path(r'^api-token-auth/$',views.obtain_auth_token), # post 方法
    # path('admin/', admin.site.urls),
    re_path(r'^api/v1/users/',include('users.urls')),
    
    re_path(r'^api/v1/articles/', include('article.urls')),
    re_path(r'^api/v2/articles/', include('article.urls')),
    
    
    re_path(r'^api/v1/utils/',include('utils.urls')),
    re_path(r'^api/v1/auths/',include('auths.urls')),
    
    
    # re_path(r'^api/v1/auth/',include('auth.urls')),
    
    
    re_path(r'media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]
