from django.contrib import admin
from .models import AdminProfile, Category, Article

admin.site.register(AdminProfile)
admin.site.register(Category)
admin.site.register(Article)
