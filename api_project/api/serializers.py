from rest_framework import serializers
from .models import Book

#BookSerializer class that extends rest_framework.serializers.ModelSerializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
