### Delete Operation - Delete Book Instance

Command:
```python

from bookshelf.models import Book

# Retrieve the book to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm the deletion
books = Book.objects.all()
print(books)
