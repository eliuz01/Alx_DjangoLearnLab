""" 
A view in django is a a function or a class that 
 -accepts a http reques
 -retuns a http response
"""
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all() # Query all books from the database

    #Render the 'list_books.html' template and pass the books as context
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view (CBV) to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library  # This CBV will work with the Library model
    template_name = 'relationship_app/library_detail.html'  # Template to render the library details
    context_object_name = 'library'  # The context variable for the template
    
