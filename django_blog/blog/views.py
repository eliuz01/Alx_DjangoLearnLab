from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, UserUpdateForm
from django.contrib import messages
from .models import Post
from django.views.generic.detail import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse

# Create your views here.

@login_required
def user_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('user_profile')  # Redirect to the same page after form submission
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

def register(request):
    return render(request, 'register.html')

class PostListView(LoginRequiredMixin, ListView):
    login_url = 'login/'
    redirect_field_name = 'login'
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    context_object_name = 'post'

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    context_object_name = 'post'

    # Custom method that determines if the user can update the post
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    context_object_name = 'post'