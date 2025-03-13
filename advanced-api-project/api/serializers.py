from .models import Book, Author
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:  #defines the behavior and settings for the serializer
        model = Book
        fields = '__all__'
    
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Author
        fields = 'name'
    
    def bo



