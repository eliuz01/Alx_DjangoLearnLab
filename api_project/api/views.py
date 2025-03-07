from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Book
from .serializers import BookSerializer 

# Create your views here.
class BookList(generics.ListAPIView):
    """
    API endpoint to list all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint for CRUD operations on books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


