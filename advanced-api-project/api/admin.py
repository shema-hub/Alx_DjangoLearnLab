from django.contrib import admin
from .models import Author, Book
# Register your models here.

# Author Admin
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

# Book Admin
@admin.register(Book)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
