from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model

# Get the custom user model
User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    # Nesting the author field to return username instead of user id
    author = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']
    
    def validate_title(self, value):
        """Ensure title is not empty."""
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_content(self, value):
        """Ensure content is not empty."""
        if not value.strip():
            raise serializers.ValidationError("Content cannot be empty.")
        return value


class CommentSerializer(serializers.ModelSerializer):
    # Nesting the author field to return username instead of user id
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())  # Post reference
    
    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'content', 'created_at', 'updated_at']
    
    def validate_content(self, value):
        """Ensure comment content is not empty."""
        if not value.strip():
            raise serializers.ValidationError("Comment content cannot be empty.")
        return value
