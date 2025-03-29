from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import permissions, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action


# Create your views here.
class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow the author of the post/comment to edit or delete it.
    """
    def has_object_permission(self, request, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of the post/comment
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        # Automatically set the author to the currently authenticated user
        serializer.save(author=self.request.user)

    def get_queryset(self):
        # Optionally filter posts for a specific user (e.g., for a profile view)
        user = self.request.user
        following_users = user.following.all()  
        return Post.objects.filter(author__in=following_users).order_by('-created_at') 
    
    @action(detail=False, methods=['get'])
    def feed(self, request):
        user = request.user
        following_users = user.following.all()  # **Get users the current user is following**

        feed_posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = self.get_serializer(feed_posts, many=True)
        
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        # Automatically set the author to the currently authenticated user
        post = serializer.validated_data['post']
        if not post:
            raise PermissionDenied("Comment must be associated with a valid post.")
        serializer.save(author=self.request.user)

    def get_queryset(self):
        # Optionally filter comments for a specific user or post
        post_id = self.request.query_params.get('post_id')
        if post_id:
            return Comment.objects.filter(post_id=post_id)
        return Comment.objects.all()
