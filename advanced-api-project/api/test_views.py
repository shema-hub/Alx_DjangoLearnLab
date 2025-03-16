from django.test import APITestCase, RequestFactory, APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status 
from rest_framework.test import force_authenticate
from .models import Book, Author
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
class BookAPITests(APITestCase):
    def setUp(self):
        self.factory = RequestFactory()  # Initialize RequestFactory
        self.user = User.objects.create_user(username="deelan", password="1609@Kilel")
        self.client = APIClient()

        # Log in the test user
        self.client.login(username='deelan', password='1609@Kilel')

        # Create test authors
        self.author1 = Author.objects.create(name="deelan")
        self.author2 = Author.objects.create(name="chepchumba winny")

        # Create test books
        self.book1 = Book.objects.create(title="Kiki", publication_year=2014, author=self.author1)
        self.book2 = Book.objects.create(title="Hello World", publication_year=2020, author=self.author2)

    # Test Create Book
    def test_create_book(self):
        url = reverse('book-create')
        data = {'title': 'New Book', 'publication_year': 2024, 'author': self.author1.id}
        request = self.factory.post(url, data)
        force_authenticate(request, user=self.user)  # Authenticate user
        response = BookCreateView.as_view()(request)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Use DRF status codes
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(response.data['title'], 'New Book')  # Ensure response contains expected data

    # Test Retrieve Book
    def test_retrieve_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        request = self.factory.get(url)
        force_authenticate(request, user=self.user)
        response = BookDetailView.as_view()(request, pk=self.book1.id)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Kiki')  # Ensure response contains correct book title

    # Test Update Book
    def test_update_book(self):
        url = reverse('book-update', args=[self.book1.id])
        data = {'title': 'Updated Book', 'publication_year': 2025, 'author': self.author2.id}
        request = self.factory.put(url, data)
        force_authenticate(request, user=self.user)
        response = BookUpdateView.as_view()(request, pk=self.book1.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')  # Ensure book title was updated

    # Test Delete Book
    def test_delete_book(self):
        url = reverse('book-delete', args=[self.book1.id])
        request = self.factory.delete(url)
        force_authenticate(request, user=self.user)
        response = BookDeleteView.as_view()(request, pk=self.book1.id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)  # Ensure book was deleted

    # Test Filtering
    def test_filter_books(self):
        url = reverse('book-list')
        request = self.factory.get(url, {'author': self.author1.id})
        force_authenticate(request, user=self.user)
        response = BookListView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Kiki', str(response.data))  # Ensure response contains filtered book

    # Test Searching
    def test_search_books(self):
        url = reverse('book-list')
        request = self.factory.get(url, {'search': 'Kiki'})
        force_authenticate(request, user=self.user)
        response = BookListView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Kiki', str(response.data))  # Ensure search returns correct book

    # Test Ordering
    def test_order_books(self):
        url = reverse('book-list')
        request = self.factory.get(url, {'ordering': 'publication_year'})
        force_authenticate(request, user=self.user)
        response = BookListView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = [book['title'] for book in response.data]
        self.assertEqual(response_data, ['Kiki', 'Hello World'])  # Ensure books are ordered by year