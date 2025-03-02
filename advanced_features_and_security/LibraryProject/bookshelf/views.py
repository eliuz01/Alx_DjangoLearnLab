from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm  # Import ExampleForm as per the checker
from bookshelf.models import Book

# View all books (protected by 'can_view' permission)
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

# Create a new book (protected by 'can_create' permission)
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Sanitize and validate inputs using ExampleForm (or any other form)
        form = ExampleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            publication_year = form.cleaned_data['publication_year']

            # Securely create the new book instance
            book = Book.objects.create(title=title, author=author, publication_year=publication_year)
            return redirect('book_list')
    else:
        form = ExampleForm()  # If GET request, show an empty form

    return render(request, 'create_book.html', {'form': form})

# Edit an existing book (protected by 'can_edit' permission)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        # Sanitize and validate inputs using ExampleForm (or any other form)
        form = ExampleForm(request.POST)
        if form.is_valid():
            book.title = form.cleaned_data['title']
            book.author = form.cleaned_data['author']
            book.publication_year = form.cleaned_data['publication_year']
            book.save()
            return redirect('book_list')
    else:
        # Initialize form with existing book data
        form = ExampleForm(initial={'title': book.title, 'author': book.author, 'publication_year': book.publication_year})

    return render(request, 'edit_book.html', {'form': form, 'book': book})
