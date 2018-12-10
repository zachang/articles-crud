from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Article, Category

class AdminSerializer(serializers.ModelSerializer):
    """A serializer for Admin profile object"""
    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'articles')
        extra_kwargs = {'password': {'write_only': True}}

class ArticleSerializer(serializers.ModelSerializer):
    """A serializer for Article object"""
    user = serializers.ReadOnlyField(source='user.id')
    category = serializers.ReadOnlyField(source='categories.id')

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'category', 'user')
        

class CategorySerializer(serializers.ModelSerializer):
    """A serializer for Category object"""

    class Meta:
        model = Category
        fields = ('id', 'category_name')
