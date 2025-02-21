from django.contrib import admin

# Register your models here.

from .models import Book  # Import the Book model

# Register the Book model with default settings
#admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display fields in the list view
    list_display = ("title", "author", "publication_year")

    # Add search functionality (search by title and author)
    search_fields = ("title", "author")

    # Add filters (filter by publication year)
    list_filter = ("publication_year",)
