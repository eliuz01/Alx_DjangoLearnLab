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

class UserProfile(models.Model):
# Define the roles
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]


    # Link the UserProfile to the User model with a OneToOneField
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    