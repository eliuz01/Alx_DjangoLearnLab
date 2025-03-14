from .models import Book, Author
from rest_framework import serializers
from django.core.exceptions import ValidationError
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:  #defines the behavior and settings for the serializer
        model = Book #the database table with data to be serialized 
        fields = '__all__' #the data fields to be serialized in the table Book
    
    def validate_publication_year(self, data):#the validate_field() method takes the field tame followed by two arguents, i.e. instance and data representing the field
        current_year = datetime.now().year#declares a variable that takes the value of urrent year
        if data > current_year:
            raise serializers.ValidationError(f"the publication error cannot be in the future")
        return data
    
class AuthorSerializer(serializers.ModelSerializer):
    related_books = BookSerializer["(many=True, read_only=True)"]
    class Meta:#defines the behavior and settings for the serializer
        model  = Author #the database table with data to be serialized 
        fields = ("name", "related_books") #the data fields to be serialized in the table Author
    
  






