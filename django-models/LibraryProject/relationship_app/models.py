from django.db import models

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
