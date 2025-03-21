# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import User_Profile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ['bio', 'avatar']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
