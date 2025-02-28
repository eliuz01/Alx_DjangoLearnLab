from django.db import models
from django.contrib.auth.models import AbstractUser 

 

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField() 


# Create your models here.
#uses inheritance  
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(("Date of Birth"), auto_now=False, auto_now_add=False, null=False)
    profile_photo = models.ImageField(("Profile Photo"), upload_to=None, height_field=None, width_field=None, max_length=100, null=True)