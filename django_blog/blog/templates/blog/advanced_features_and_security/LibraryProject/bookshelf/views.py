from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from .models import Book
from .forms import ExampleForm  # Import Django Form for validation

@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book successfully created!")
            return redirect("book_list")  # Redirect instead of reloading template
        else:
            messages.error(request, "Error in form submission. Please check the fields.")
    else:
        form = ExampleForm()
    
    return render(request, "bookshelf/form_example.html", {"form": form})

@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        form = ExampleForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book details updated successfully!")
            return redirect("book_list")
        else:
            messages.error(request, "Error in form submission. Please check the fields.")
    else:
        form = ExampleForm(instance=book)

    return render(request, "bookshelf/form_example.html", {"form": form, "book": book})

@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    messages.success(request, "Book deleted successfully!")
    return redirect("book_list")
