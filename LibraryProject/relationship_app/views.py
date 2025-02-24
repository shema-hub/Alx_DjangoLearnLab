from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from .models import Book
from .forms import BookForm  # You'll need to create this form

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'ADMIN'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'LIBRARIAN'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'MEMBER'

@user_passes_test(is_admin, login_url='login')
def admin_view(request):
    return render(request, 'admin_dashboard.html', {
        'title': 'Admin Dashboard',
        'message': 'Welcome to Admin Dashboard'
    })

@user_passes_test(is_librarian, login_url='login')
def librarian_view(request):
    return render(request, 'librarian_dashboard.html', {
        'title': 'Librarian Dashboard',
        'message': 'Welcome to Librarian Dashboard'
    })

@user_passes_test(is_member, login_url='login')
def member_view(request):
    return render(request, 'member_dashboard.html', {
        'title': 'Member Dashboard',
        'message': 'Welcome to Member Dashboard'
    })

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books}) 
