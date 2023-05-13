from rest_framework import serializers

from .models import (
    Article,
    Nav1,
    Nav2
)

class ArticleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class Nav1ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nav1
        fields = '__all__'


class Nav2ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nav2
        fields = '__all__'


