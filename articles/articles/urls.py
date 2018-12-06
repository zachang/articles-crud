from django.contrib import admin
from django.urls import path, include
from blog.views import login

urlpatterns = [
    path('blog/api/', include('blog.urls')),
    path('blog/api/login/', login),
    path('admin/', admin.site.urls),
]
