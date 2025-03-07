from django.urls import path, include
from .views import BookList, BookViewSet, AnotherBookViewSet
from rest_framework import DefaultRouter

router = DefaultRouter()
router.register(r'book_all', BookViewSet, basename='book_all')
router.register(r'another-models', AnotherBookViewSet)

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('', include(router.urls)), # This includes all routes registered with the router
]