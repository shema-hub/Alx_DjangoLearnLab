from django.urls import path
from .views.admin_view import admin_view
from .views.librarian_view import librarian_view
from .views.member_view import member_view

urlpatterns = [
    path('admin-dashboard/', admin_view, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_view, name='librarian_dashboard'),
    path('member-dashboard/', member_view, name='member_dashboard'),
] 