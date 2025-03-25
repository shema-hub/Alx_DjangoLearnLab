from django.contrib import admin
from .models import Post, Comment

# Register your models here.
# Register the Profile Model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content')