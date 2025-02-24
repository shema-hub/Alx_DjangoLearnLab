from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'ADMIN'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'LIBRARIAN'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'MEMBER'

@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Admin Dashboard - Restricted Access")

@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Librarian Dashboard - Restricted Access")

@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Member Dashboard - Restricted Access") 