from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.models import BaseUserManager

 

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField() 

#Create custom user manager
class CustomUserManager(BaseUserManager):
    def create_user(self, date_of_birth, profile_photo):
        if not date_of_birth:
            raise ValueError("Date of Birth Needed")
        user = self.model(date_of_birth=date_of_birth)
        user = self.model(profile_photo=profile_photo)
        user.save(using=self._db)

        return user
    def create_superuser(self, date_of_birth, profile_photo):
        user = self.create_user(date_of_birth, profile_photo)
        
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

# Create your models here.
#uses inheritance  
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(("Date of Birth"), auto_now=False, auto_now_add=False, null=False)
    profile_photo = models.ImageField(("Profile Photo"), upload_to=None, height_field=None, width_field=None, max_length=100, null=True)