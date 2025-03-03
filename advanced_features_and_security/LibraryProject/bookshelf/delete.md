from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Try retrieving all books to confirm deletion
books = Book.objects.all()
print(f"Total Books: {books.count()}")

#Expected Output:
#Total Books: 0 (if this was the only book in the database)
