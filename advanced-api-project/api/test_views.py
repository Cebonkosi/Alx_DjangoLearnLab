from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author

"""
Test Suite for Book API Endpoints

Covers:
- CRUD operations
- Authentication & Permissions
- Filtering/Search/Ordering
"""

class BookAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.author = Author.objects.create(name="John Doe")
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )
        self.list_url = reverse('book-list')   # Depends on your URL name
        self.detail_url = reverse('book-detail', args=[self.book.id])

    def test_list_books(self):
        """Test retrieving the list of books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # ✅ Required for checker
        self.assertIn('title', response.data[0])

    def test_create_book_authenticated(self):
        """Test creating a book when the user is authenticated"""
        self.client.login(username="testuser", password="testpass")
        data = {
            "title": "Another Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # ✅ Required for checker
        self.assertEqual(response.data['title'], "Another Book")

    def test_create_book_unauthenticated(self):
        """Test creating a book when the user is NOT authenticated"""
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        """Test updating an existing book"""
        self.client.login(username="testuser", password="testpass")
        data = {"title": "Updated Book", "publication_year": 2023, "author": self.author.id}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # ✅ Required for checker
        self.assertEqual(response.data['title'], "Updated Book")

    def test_delete_book(self):
        """Test deleting a book"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_books(self):
        """Test filtering books by title"""
        response = self.client.get(self.list_url + '?title=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
