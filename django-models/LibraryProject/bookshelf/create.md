### Create Operation - Book Instance Creation

Command:
```python
from yourapp.models import Book

# Create a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()
