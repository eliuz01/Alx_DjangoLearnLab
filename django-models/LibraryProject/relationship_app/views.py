from django.shortcuts import render
from django.http import HttpResponse  # Import HttpResponse
from django.views.generic import DetailView
from .models import Book
from .models import Library

# Function-based view to list all books


def list_books(request):
    books = Book.objects.all() # Query all books from the database

    #Render the 'list_books.html' template and pass the books as context
    return render(request, 'relationship_app/list_books.html', {'books': books})

def home(request):
    return HttpResponse("Welcome to the Library Homepage!")

# Class-based view (CBV) to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library  # This CBV will work with the Library model
    template_name = 'library_detail.html'  # Template to render the library details
    context_object_name = 'library'  # The context variable for the template
    
    # Optionally, you can override get_context_data to add extra context to the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Get the default context data
        return context