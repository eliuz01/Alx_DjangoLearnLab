from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ['password', 'bio', 'profile_picture', 'followers']

    def create(self, validated_data):
        # Create user and hash the password
        password = validated_data.pop('password', None)
        user = get_user_model().objects.create_user(**validated_data)
        
        # Hash the password and save the user
        if password:
            user.set_password(password)
            user.save()

        # Create the token for the user
        Token.objects.create(user=user)

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        # Use authenticate() to verify the user's credentials
        user = authenticate(username=data['username'], password=data['password'])

        if user is None:
            raise serializers.ValidationError("Invalid username or password")

        return {'user': user}

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_picture']