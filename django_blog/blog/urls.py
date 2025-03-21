from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout.html'),
    path('register/', views.register, name='register.html'),
    path('profile/', views.user_profile, name='profile.html'),    
    path('post_list/', PostListView.as_view(), name='post_list.html'),
    path('post_detail/', PostDetailView.as_view(), name='post_detail.html'),
    path('post/new/', PostCreateView.as_view(), name='post_create.html'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update.html'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete.html'),
]

