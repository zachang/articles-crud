from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'admin', views.AdminViewset)
router.register(r'article', views.ArticleViewset)


urlpatterns = [
    path('index/', views.index, name='index'),
    path('', include(router.urls)),
]