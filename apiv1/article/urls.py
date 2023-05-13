
from django.urls import path,include,re_path
from rest_framework import routers
from .views import (
    ArticleModelViewsets,
    Nav1ModelViewsets,
    Nav2ModelViewsets,
)

router = routers.SimpleRouter(trailing_slash=False)

urlpatterns = [
    re_path(r"^nav1$",Nav1ModelViewsets.as_view({"get":"list","post":"create"}),name='nav1'),
    re_path(r"^nav1/(?P<id>.+)$",Nav1ModelViewsets.as_view({"get":"retrieve","put":"update","patch":"partial_update","delete":"destroy"}),name='nav1_'),

    
    re_path(r"^nav2$",Nav2ModelViewsets.as_view({"get":"list","post":"create"}),name='nav2'),
    re_path(r"^nav2/(?P<id>.+)$",Nav2ModelViewsets.as_view({"get":"retrieve","put":"update","patch":"partial_update","delete":"destroy"}),name='nav2_'),
]

router.register(r'',ArticleModelViewsets)
urlpatterns += router.urls

