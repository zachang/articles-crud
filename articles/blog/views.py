from django.shortcuts import render
from django.http import Http404
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from django.http import HttpResponse

from . import serializers
from .permissions import IsOwnerOrReadOnly
from .models import Article, Category
from .utils import CustomAPIException


def index(request):
    return HttpResponse("Hello, world. You're at the blogs index.")


class AdminViewset(viewsets.ModelViewSet):
    queryset =  User.objects.all()
    serializer_class = serializers.AdminSerializer
    permission_classes = (AllowAny,)


    def create(self, request, *args, **kwargs):
        serializer = serializers.AdminSerializerWithToken(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'user': serializer.data}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                category = Category.objects.get(pk=request.data['category'])
                serializer.save(user=self.request.user, category_id=category.id)
                return Response({'articles': serializer.data}, status=HTTP_201_CREATED)
            except Category.DoesNotExist:
                raise CustomAPIException("This Category does not exist", 
                    status_code=HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
