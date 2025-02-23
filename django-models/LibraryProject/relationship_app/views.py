from django.shortcuts import render
from .models import Book







# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # This fetches all the books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})



from django.views.generic import DetailView
from .models import Library

# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
