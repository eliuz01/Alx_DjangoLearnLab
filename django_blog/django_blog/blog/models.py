from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(("Title"), max_length=200)
    content = models.TextField(("Content"))
    published_date = models.DateTimeField(("Published Date"), auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title