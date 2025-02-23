from django.urls import path
from . import views 
from views import list_books, LibraryDetailView

urlpatterns = [
    # URL for function-based view to list books
    path('books/', views.list_books, name='list_books'),

    # URL for class-based view to display library details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
