from django.db import models

# Create your models here.
class Author(models.Model): #creates model author that represents a table in database
    name = models.CharField(("Name"), max_length=100) #created the field "name", which will be a column in the database table calledauthor


class Book(models.Model):#creates model Book that represents a table in database
    title = models.CharField(("Title"), max_length=100)
    publication_year = models.IntegerField(("Publication Date"))
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
'''
The fields title, publication_year, and author will be columns in the database table called Books
'''
    
