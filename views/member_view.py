from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'MEMBER'

@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("This page is only accessible to Members") 