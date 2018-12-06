from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.http import HttpResponse
from . import serializers


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class AdminViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.AdminSerializer
