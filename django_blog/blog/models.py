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

class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # Link to Post
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')  # Link to User
    content = models.TextField()  # Comment content
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set when updated

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"