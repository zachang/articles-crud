from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class AdminProfile(models.Model):  
    """Represents UserProfile model class"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):  
          return "{}'s profile".format(self.user,)

def create_admin_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = AdminProfile.objects.get_or_create(user=instance)  

post_save.connect(create_admin_profile, sender=User)

class Category(models.Model):
    """Represents Category model class"""

    category_name = models.CharField(max_length=255)

    def __str__(self):  
         return self.category_name 


class Article(models.Model):
    """Represents News model class"""

    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name="categories", on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, related_name="articles", on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=255)
    image = models.CharField(max_length=255)

    def __str__(self):  
         return self.title 
