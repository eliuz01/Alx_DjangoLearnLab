```python
# Retrieve all books from the database
books = Book.objects.all()
print(books)

# Retrieve the specific book by title

books = Book.objects.get(title="1984")
print(book)
