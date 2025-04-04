from django.urls import path, include
from .views import UserRegistrationView, UserLoginView, FollowViewSet, follow_user, unfollow_user
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    
    # Correct follow/unfollow endpoints
    path('follow/<int:user_id>/', follow_user, name='follow'), 
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow'),
]