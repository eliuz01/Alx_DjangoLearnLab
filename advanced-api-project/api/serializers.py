from .models import Book, Author
from rest_framework import serializers
from django.core.exceptions import ValidationError
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:  #defines the behavior and settings for the serializer
        model = Book
        fields = '__all__'
    
    def validate_publicaion_year(self, data):
        current_year = datetime.now().year
        if data > current_year:
            raise serializers.ValidationError(f"the publication error cannot be in the future")
        return data
    
class AuthorSerializer(serializers.ModelSerializer):
    related_books = BookSerializer(many=True, read_only = True)
    class Meta:
        model  = Author 
        fields = ("name", "related_books")
    
  






