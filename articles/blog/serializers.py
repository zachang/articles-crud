from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from .models import Article, Category


class AdminSerializer(serializers.ModelSerializer):
    """A serializer for Admin profile object"""
    articles = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'articles')


class AdminSerializerWithToken(serializers.ModelSerializer):
    """A serializer for Admin profile object with jwt rendered"""
    token = serializers.SerializerMethodField()
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'token')
        extra_kwargs = {'password': {'write_only': True}}


    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()    
        return user

class ArticleSerializer(serializers.ModelSerializer):
    """A serializer for Article object"""
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'category', 'user')


class CategorySerializer(serializers.ModelSerializer):
    """A serializer for Category object"""

    class Meta:
        model = Category
        fields = ('id', 'category_name')
