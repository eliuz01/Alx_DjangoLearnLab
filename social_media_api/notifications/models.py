from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Get the custom user model
User = get_user_model()

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')  # User receiving the notification
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actions')  # User performing the action
    verb = models.CharField(max_length=255)  # Action description (e.g., "liked", "commented", "followed")
    
    # Generic ForeignKey to associate the notification with any object (Post, Comment, etc.)
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Content type of the target object
    target_object_id = models.PositiveIntegerField()  # ID of the target object (e.g., Post, Comment, etc.)
    target = GenericForeignKey('target_content_type', 'target_object_id')  # The actual target object (Post, Comment, etc.)

    timestamp = models.DateTimeField(auto_now_add=True)  # When the notification was created

    def __str__(self):
        return f'Notification for {self.recipient.username} by {self.actor.username}: {self.verb} {self.target}'
