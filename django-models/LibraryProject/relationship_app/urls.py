from django.urls import path
from .views import list_books, LibraryDetailView, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL for listing all books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for library details
    path('register/', register, name='register'),  # URL for user registration
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # URL for login
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),  # URL for logout
]
