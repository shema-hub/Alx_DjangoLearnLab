from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="1984")

# Display book attributes
print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")

#Expected Output:
#Title: 1984, Author: George Orwell, Publication Year: 1949
