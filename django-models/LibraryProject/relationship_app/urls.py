from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from relationship_app import views
from .views import list_books, LibraryDetailView, librarian_view




urlpatterns = [
    path('books/', views.list_books, name='list_books'), # FBV for listing books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # CBV for library details
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # LoginView with a custom template
    path('logout/', LogoutView.as_view(template_name='login.html'), name='logout'),  # LogoutView, no custom template needed
    path('register/', views.register, name='register'),  # URL for registration page
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),  # URL for adding a book
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),  # URL for editing a book, using the book's primary key
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),  # URL for deleting a book, using the book's primary key
]
