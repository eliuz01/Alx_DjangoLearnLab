### Update Operation - Update Book Title

Command:
```python
# Retrieve the book to update
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm the update
print(book)
