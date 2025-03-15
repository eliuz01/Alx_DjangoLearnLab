from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author
#generic views provide commonly needed behaviours such as creat,list, read, delete, which are model instances
# Create your views here.
"""Action Items:
Implement a set of generic views for the Book model to handle CRUD operations. This includes:
A ListView for retrieving all books.
A DetailView for retrieving a single book by ID.
A CreateView for adding a new book.
An UpdateView for modifying an existing book.
A DeleteView for removing a book."""
#create class begin with model name 'Book' followed by th behaviour i.e. ListView or CreateView....
class BookListView(generics.ListAPIView ): 
     queryset = Book.objects.all()
     serializer_class = BookSerializer

class BookDetailView(generics.DetailAPIView ): 
     queryset = Book.objects.get(id)
     serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView ): 
     queryset = Book.objects.create()
     serializer_class = BookSerializer

class BookUpdateView(generics.UpdateAPIView): 
     queryset = Book.objects.update()
     serializer_class = BookSerializer

class BookDeleteView(generics.DeleteAPIView ): 
     queryset = Book.objects.delete()
     serializer_class = BookSerializer