from django.shortcuts import render
from .models import Book


from django.views.generic.detail import DetailView
from .models import Library

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView







# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # This fetches all the books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})





# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'





# Custom view for user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after successful registration
            return redirect('list_books')  # Redirect to a page after registration (can be changed)
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login view (using Django's built-in LoginView)
class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout view (using Django's built-in LogoutView)
class UserLogoutView(LogoutView):
    next_page = 'login'  # Redirect to login page after logout
