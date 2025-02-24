from django.db import models
from django.contrib.auth.models import User

# Advanced Model Relationships 

class Author(models.Model):
    name = models.CharField("Name", max_length=200)

    def __str__(self):
        return self.name  # Returns the name of the author

class Book(models.Model):
    title = models.CharField("Title", max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title  # Returns the title of the book

class Library(models.Model):
    name = models.CharField(max_length=200)
    book = models.ManyToManyField("relationship_app.Book", verbose_name="Book")

    def __str__(self):
        return self.name  # Returns the name of the library

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name  # Returns the name of the librarian

# User Profile Model
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Signal to automatically create UserProfile when a new user is created
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()