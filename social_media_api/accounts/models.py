from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager, PermissionsMixin
from django.conf import settings

# Custom user model manager where email is the unique identifier
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

# CustomUser model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to="profile_pictures/", null=True, blank=True)
    followers = models.ManyToManyField("self", symmetrical=False, blank=True, related_name='user_following')
    following = models.ManyToManyField("self", symmetrical=False, blank=True, related_name='user_followers')
    is_active = models.BooleanField(default=True)  
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    def follow(self, user):
        """Follow another user"""
        if user != self and not self.following.filter(id=user.id).exists():
            self.following.add(user)
            return True
        return False

    def unfollow(self, user):
        """Unfollow a user"""
        if user != self and self.following.filter(id=user.id).exists():
            self.following.remove(user)
            return True
        return False