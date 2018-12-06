from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User

class AdminSerializer(serializers.ModelSerializer):
    """A serializer for Admin profile object"""

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

class ArticleSerializer(serializers.ModelSerializer):
    """A serializer for Admin profile object"""

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'category_id', 'user_id')

