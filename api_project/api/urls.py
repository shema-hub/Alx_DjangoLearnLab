from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='allbooks')

urlpatterns = [
    path('books/', BookList.as_view(), name='booklist'),
    path('', include(router.urls)),
]
