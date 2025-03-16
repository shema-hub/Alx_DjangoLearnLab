from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseForbidden
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework
from rest_framework import generics

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    fields = ['title', 'publication_year', 'author']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year', 'author']
    ordering = ['title']

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

class BookCreateView(CreateView):
    model = Book
    template_name = 'book_create.html'
    fields = ['title', 'author', 'description', 'published_date']

    def dispatch(self, request, *args, **kwargs):
        permission = IsAuthenticated()
        if not permission.has_permission(request, self):
            return HttpResponseForbidden("You don't have permission to create a book.")
        return super().dispatch(request, *args, **kwargs)

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_update.html'
    fields = ['title', 'author', 'description', 'published_date']

    def dispatch(self, request, *args, **kwargs):
        permission = IsAuthenticatedOrReadOnly()
        if not permission.has_permission(request, self):
            return HttpResponseForbidden("You don't have permission to update this book.")
        return super().dispatch(request, *args, **kwargs)

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        permission = IsAuthenticated()
        if not permission.has_permission(request, self):
            return HttpResponseForbidden("You don't have permission to delete this book.")
        return super().dispatch(request, *args, **kwargs)
