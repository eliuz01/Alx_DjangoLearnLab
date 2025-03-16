from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author

# Custom filter for Book model
class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')  # Allows case-insensitive partial match for title
    author = filters.CharFilter(field_name='author__name', lookup_expr='icontains')  # Allows search by author name
    publication_year = filters.NumberFilter(lookup_expr='exact')  # Allows filtering by publication year

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']


# BookListView with ordering (ONLY OrderingFilter from filters)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()  # Get all Book objects
    serializer_class = BookSerializer  # Specify the serializer for Book model
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow authenticated users or read-only access

    # Use ONLY filters.OrderingFilter as requested
    filter_backends = [filters.OrderingFilter]  # Just use OrderingFilter here (no other filters)

    # Define which fields can be used for ordering
    ordering_fields = ['title', 'publication_year']  # Allow ordering by 'title' or 'publication_year'

    # Set default ordering (e.g., order by title by default)
    ordering = ['title']  # Default ordering by 'title'

# The other views remain the same as they handle create, update, delete, and retrieve
class BookDetailView(generics.DetailAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
