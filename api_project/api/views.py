from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

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

class MyApiView(APIView):
    authentication_classes =  [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'Hello, athenticated user!'})






