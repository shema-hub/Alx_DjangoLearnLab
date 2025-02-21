from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Retrieve the updated book to confirm changes
updated_book = Book.objects.get(id=book.id)
print(f"Updated Title: {updated_book.title}")

#Expected Output:
#Updated Title: Nineteen Eighty-Four
