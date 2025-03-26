from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

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
