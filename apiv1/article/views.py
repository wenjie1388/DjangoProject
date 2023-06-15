from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from .models import (
    Article,
    Nav1,
    Nav2,
)

from rest_framework.authentication import SessionAuthentication,BaseAuthentication
from .serializers import (
    ArticleModelSerializer,
    Nav1ModelSerializer,
    Nav2ModelSerializer,
)

class ArticleModelViewsets(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
    lookup_field = "id"
    authentication_classes = [BaseAuthentication]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    

class ArticleCardView(mixins.ListModelMixin,GenericViewSet):
    pass

class Nav1ModelViewsets(viewsets.ModelViewSet):
    
    queryset = Nav1.objects.all()
    serializer_class = Nav1ModelSerializer
    lookup_field = "id"

class Nav2ModelViewsets(viewsets.ModelViewSet):
    queryset = Nav2.objects.all()
    serializer_class = Nav2ModelSerializer
    lookup_field = "id"


