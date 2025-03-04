from django.db import models

# Create your models here.
class Book(models.Model):
    titie  = models.CharField(("Title"), max_length=200)
    author  = models.CharField(("Author"), max_length=100)
    published_date = models.DateField(("Published Date"))