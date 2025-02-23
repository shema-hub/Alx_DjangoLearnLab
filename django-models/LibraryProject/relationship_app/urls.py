from django.urls import path
from .views import list_books, LibraryDetailView, register, UserLoginView, UserLogoutView
from .views import list_books, LibraryDetailView, register, UserLoginView, UserLogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL for listing all books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for library details
    path('register/', register, name='register'),  # URL for user registration
    path('login/', UserLoginView.as_view(), name='login'),  # URL for login
    path('logout/', UserLogoutView.as_view(), name='logout'),  # URL for logout
]
