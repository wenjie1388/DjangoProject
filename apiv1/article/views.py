from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import (
    Article,
    Nav1,
    Nav2,
)


from .serializers import (
    ArticleModelSerializer,
    Nav1ModelSerializer,
    Nav2ModelSerializer,
)


class ArticleModelViewsets(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
    lookup_field = "id"

class Nav1ModelViewsets(viewsets.ModelViewSet):
    
    queryset = Nav1.objects.all()
    serializer_class = Nav1ModelSerializer
    lookup_field = "id"

class Nav2ModelViewsets(viewsets.ModelViewSet):
    queryset = Nav2.objects.all()
    serializer_class = Nav2ModelSerializer
    lookup_field = "id"






