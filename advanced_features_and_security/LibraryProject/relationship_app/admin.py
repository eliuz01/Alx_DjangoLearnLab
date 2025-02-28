# relationship_app/admin.py
from django.contrib import admin
from .models import Author, Book, Library, Librarian

# Register the Author model
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the author's name in the list
    search_fields = ('name',)  # Allow searching by name

# Register the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')  # Display the book title and author in the list
    search_fields = ('title', 'author__name')  # Allow searching by book title and author name
    list_filter = ('author',)  # Filter by author

# Register the Library model
@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the library's name in the list
    search_fields = ('name',)  # Allow searching by library name
    filter_horizontal = ('book',)  # Add a horizontal filter for selecting books in the library

# Register the Librarian model
@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', 'library')  # Display librarian name and the associated library
    search_fields = ('name', 'library__name')  # Allow searching by librarian name and library name
