from django.shortcuts import render, redirect
from django.contrib.auth import login, logout  
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from .models import Library, Book  
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm

def home(request):
    return redirect("list_books") 

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  

            if hasattr(user, "userprofile"):
                if user.userprofile.role == "Admin":
                    return redirect("admin_view")
                elif user.userprofile.role == "Librarian":
                    return redirect("librarian_view")
                elif user.userprofile.role == "Member":
                    return redirect("member_view")
            return redirect("home")  # Default redirect

    else:
        form = UserCreationForm()
    
    return render(request, "relationship_app/register.html", {"form": form})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"

class UserLoginView(LoginView):
    template_name = "relationship_app/login.html"

class UserLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"  

# Role checking functions with better error handling
def is_admin(user):
    return user.is_authenticated and getattr(user, "userprofile", None) and user.userprofile.role == "Admin"

def is_librarian(user):
    return user.is_authenticated and getattr(user, "userprofile", None) and user.userprofile.role == "Librarian"

def is_member(user):
    return user.is_authenticated and getattr(user, "userprofile", None) and user.userprofile.role == "Member"

# Role-based views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")


@permission_required("relationship_app.can_add_book", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm()
    return render(request, "relationship_app/add_book.html", {"form": form})

@permission_required("relationship_app.can_change_book", raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm(instance=book)
    return render(request, "relationship_app/edit_book.html", {"form": form, "book": book})

@permission_required("relationship_app.can_delete_book", raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "relationship_app/delete_book.html", {"book": book})