from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'LIBRARIAN'

@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("This page is only accessible to Librarians") 