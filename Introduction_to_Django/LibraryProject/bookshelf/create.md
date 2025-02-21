from bookshelf.models import Book

book = Book.objects.create(title="George Orwelll", author="John Steinbeck", publication_year=1938 ) book.save()

Expected Output: The book instance is successfully created and saved to the database.




# Retrieve the book instance
book = Book.objects.get(title="1984")

# Display book attributes
print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")

Expected Output:
Title: 1984, Author: George Orwell, Publication Year: 1949







# Retrieve the book instance
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Retrieve the updated book to confirm changes
updated_book = Book.objects.get(id=book.id)
print(f"Updated Title: {updated_book.title}")

Expected Output:
Updated Title: Nineteen Eighty-Four








# Retrieve the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Try retrieving all books to confirm deletion
books = Book.objects.all()
print(f"Total Books: {books.count()}")

Expected Output:
Total Books: 0 (if this was the only book in the database)


