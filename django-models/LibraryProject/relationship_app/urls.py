from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import home, list_books, register, admin_view, librarian_view, member_view, LibraryDetailView


urlpatterns = [
    path("h", home, name="home"),
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    path("admin_view/", admin_view, name="admin_view"),
    path("librarian_view/", librarian_view, name="librarian_view"),
    path("member_view/", member_view, name="member_view"),
]