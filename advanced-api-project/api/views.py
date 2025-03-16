from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
#generic views provide commonly needed behaviours such as creat,list, read, delete, which are model instances
# Create your views here.
#create class begin with model name 'Book' followed by th behaviour i.e. ListView or CreateView....
class BookListView(generics.ListAPIView ): 
     queryset = Book.objects.all()
     serializer_class = BookSerializer
     permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.DetailAPIView): 
     queryset = Book.objects.get(id)
     serializer_class = BookSerializer
     lookup_field = 'id'
     permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView): 
     queryset = Book.objects.create()
     serializer_class = BookSerializer
     permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView): 
     queryset = Book.objects.update()
     serializer_class = BookSerializer
     permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DeleteAPIView): 
     queryset = Book.objects.delete()
     serializer_class = BookSerializer
     permission_classes = [IsAuthenticated]