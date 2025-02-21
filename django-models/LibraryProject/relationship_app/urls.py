from django.contrib import admin
from django.urls import path
from relationship_app import views
from .views import list_books, LibraryDetailView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.list_books, name='list_books'), # FBV for listing books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # CBV for library details
    
]
