from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import DetailView
from .models import Book, Library

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Redirect to home after successful registration
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

def list_books(request):
    """
    Function-based view to list all books
    """
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    """
    Class-based view to show library details
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
