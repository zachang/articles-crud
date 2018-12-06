from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'admin', views.AdminViewset)


urlpatterns = [
    path('index/', views.index, name='index'),
    path('', include(router.urls)),
]