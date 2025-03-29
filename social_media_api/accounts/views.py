from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework import status, generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import RegisterSerializer  # You can add a serializer for profile updates
from .models import CustomUser
from django.shortcuts import get_object_or_404


# Create your views here.
from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        # Call the parent's create method to create a user
        response = super().create(request, *args, **kwargs)
        
        # You could add extra logic here, such as sending an email, logging, etc.
        
        # Return the response with user details (excluding the password)
        return Response(response.data, status=status.HTTP_201_CREATED)
    
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        # Deserialize the incoming request data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Retrieve the validated user object
        user = serializer.validated_data['user']

        # Get or create a token for the authenticated user
        token, created = Token.objects.get_or_create(user=user)

        # Return the token to the user
        return Response({'token': token.key}, status=status.HTTP_200_OK)

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer  # Reuse the RegisterSerializer or create a new one for profile updates
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    def get_object(self):
        # Return the currently authenticated user object
        return self.request.user

    def update(self, request, *args, **kwargs):
        # Optionally, handle any updates to the profile (e.g., bio, profile_picture)
        return super().update(request, *args, **kwargs)


class FollowUserView(generics.GenericAPIView):
    """
    API view to follow a user.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Get the user to be followed
        user_to_follow = get_object_or_404(CustomUser, username=kwargs['username'])
        
        # Check if the user is not trying to follow themselves
        if user_to_follow == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Add the followed user to the authenticated user's following
        request.user.following.add(user_to_follow)
        
        # Return success response
        return Response({"detail": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    """
    API view to unfollow a user.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Get the user to be unfollowed
        user_to_unfollow = get_object_or_404(CustomUser, username=kwargs['username'])
        
        # Check if the user is not trying to unfollow themselves
        if user_to_unfollow == request.user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Remove the followed user from the authenticated user's following
        request.user.following.remove(user_to_unfollow)
        
        # Return success response
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)

