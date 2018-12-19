from django.contrib import admin
from django.urls import path, include
from blog.views import index
from rest_framework.authtoken import views

urlpatterns = [
    path('', index),
    path('blog/api/', include('blog.urls', namespace='blog')),
    path('admin/', admin.site.urls),
    path('blog/api/login/', views.obtain_auth_token)
]
