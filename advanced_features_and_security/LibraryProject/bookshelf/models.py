from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _



 

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField() 

    class Meta:
        permissions = [("can_create", "can create a bookshelh"),
                       ("can_delete", "can delete a bookshelf"),                     
    ]

    def __str__(self):
        return self.title

#Create custom user manager
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth=None, password=None, profile_photo=None):
        """
        Creates and returns a regular user with an email, username, date_of_birth, and password.
        """
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, profile_photo=profile_photo)
        
        # Set password if provided
        if password:
            user.set_password(password)
        
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth=None, password=None, profile_photo=None):
        """
        Creates and returns a superuser with an email, username, date_of_birth, and password.
        """
        user = self.create_user(username, email, date_of_birth, password, profile_photo)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Create your models here.
#uses inheritance  
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(("Date of Birth"), null=True)
    profile_photo = models.ImageField(("Profile Photo"), upload_to="profile_photos/", null=True, blank=True)

    # To ensure the custom manager is used:
    objects = CustomUserManager()
