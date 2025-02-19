from django.db import models

# Create your models here.


#advanced Model Relationships 

class Author(models.Model):
    name = models.CharField(("Name"), max_length=200)

class Book(models.Model):
    title = models.CharField(("Title"), max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Library(models.Model):
    name = models.CharField(max_length=200)
    book = models.ManyToManyField("relationship_app.Book", verbose_name=("Book"))

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)