from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied

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