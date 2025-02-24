from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True, default=None)  # <- FIXED HERE

    class Meta:
        permissions = [
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can change a book"),
            ("can_delete_book", "Can delete a book"),
        ]

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),    # Admin role must be exactly as required
        ('LIBRARIAN', 'Librarian'),
        ('MEMBER', 'Member'),  # Member role must be exactly as required
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='MEMBER'
    )

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Signals for automatic profile creation
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()  