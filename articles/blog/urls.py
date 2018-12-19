from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from . import views

router = routers.DefaultRouter()
router.register(r'admin', views.AdminViewset)
router.register(r'article', views.ArticleViewset)
router.register(r'category', views.CategoryViewset)

app_name = 'blog'
urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_jwt_token),
]