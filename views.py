from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'ADMIN'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'LIBRARIAN'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'MEMBER'

@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Iyi page ni ya Admin gusa")

@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Iyi page ni ya Librarian gusa")

@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Iyi page ni ya Member gusa") 