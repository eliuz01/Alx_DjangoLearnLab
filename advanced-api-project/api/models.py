from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(("Name"), max_length=100)


class Book(models.Model):
    title = models.CharField(("Title"), max_length=100)
    publication_year = models.IntegerField(("Publication Date"))
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    
