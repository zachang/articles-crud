from django.contrib import admin
from django.urls import path, include
from blog.views import index

urlpatterns = [
    path('', index),
    path('blog/api/', include('blog.urls', namespace='blog')),
    path('admin/', admin.site.urls),
]
