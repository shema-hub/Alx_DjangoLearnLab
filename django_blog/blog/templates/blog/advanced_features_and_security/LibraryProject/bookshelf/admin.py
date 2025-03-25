from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from bookshelf.models import (
    CustomUser, UserProfile, Author, Book, Library, Librarian
)

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    list_display = ("email", "username", "is_staff", "is_active")
    search_fields = ("email", "username")
    ordering = ("email",)

# User Profile Admin
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "bio")
    search_fields = ("user__email", "role")

# Author Admin
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

# Book Admin
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "isbn")
    search_fields = ("title", "author__name", "isbn")

# Library Admin
class LibraryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

# Librarian Admin
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ("name", "library")
    search_fields = ("name", "library__name")

# Registering all models explicitly using admin.site.register()
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Library, LibraryAdmin)
admin.site.register(Librarian, LibrarianAdmin)
