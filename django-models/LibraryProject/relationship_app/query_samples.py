from relationship_app.models import Author, Book, Library, Librarian

#Query 1: All books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name) # Fetch the author by name
        books = Book.objects.filter(author=author) #Get all books by this author
        print(f"Books written by ({author_name}:)")
        for book in books:
            print(f" - {book.title}")  
    except Author.DoesNotExist:
        print(f"Author '{author_name}' does not exist.")

#Query 2: List all books in a specific library
def get_book_in_libary(library_name):
    try: 
        library = Library.objects.get(name=library_name) # Fetch the library by name
        books = library.books.all() # Many-to-Many relationship, get all books in this library
        print(f"Books in the library '{library_name}':")
        for book in books:
            print(f" - {book.title}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")

#Query 3: Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name = library_name) # Fetch the library by name
        librarian = Librarian.objects.get(library.library) # One-to-One relationship, get the librarian
        print(f"The librarian for the library '{library_name}' is {librarian.name}.")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' does not exist.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to the library '{library_name}'.")