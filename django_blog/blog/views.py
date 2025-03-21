from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def user_profile(request):
    return render(request, 'users/profile.html')

def register(request):
    return render(request, 'register.html')