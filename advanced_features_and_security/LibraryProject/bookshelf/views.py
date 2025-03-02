from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
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
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')

        book = Book.objects.create(title=title, author=author, publication_year=publication_year)
        return redirect('book_list')
    return render(request, 'create_book.html')

# Edit an existing book (protected by 'can_edit' permission)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return redirect('book_list')
    return render(request, 'edit_book.html', {'book': book})
