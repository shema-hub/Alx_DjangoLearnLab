from bookshelf.models import Book

book = Book.objects.create(title="George Orwelll", author="John Steinbeck", publication_year=1938 ) book.save()

Expected Output: The book instance is successfully created and saved to the database.


