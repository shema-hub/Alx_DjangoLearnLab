from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Import views module instead of individual views

urlpatterns = [
    path("", views.home, name="home"),
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
    path("register/", views.register, name="register"),  # Using views.register
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    path("admin_view/", views.admin_view, name="admin_view"),
    path("librarian_view/", views.librarian_view, name="librarian_view"),
    path("member_view/", views.member_view, name="member_view"),
]