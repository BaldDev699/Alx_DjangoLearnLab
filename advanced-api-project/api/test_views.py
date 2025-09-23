from django.test import APITestCase
from .models import Book
from rest_framework import status
from django.contrib.auth.models import User

class BookModelTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            published_year=2023
        )
        self.list_url = '/api/books/list/'
        self.detail_url = f'/api/books/{self.book.id}/detail/'
    
    def test_book_creation(self):
        data = {
            "title": "New Book",
            "author": "New Author",
            "published_year": 2024
        }
        response = self.client.post('/api/books/create/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, "New Book")
    
    def test_book_list(self):
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_book_detail(self):
        response = self.client.get(self.detail_url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], "Test Book")

    def test_book_update(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.detail_url, format='json')
        data = {
            "title": "Updated Book",
            "author": "Updated Author",
            "published_year": 2025
        }
        response = self.client.put(f'/api/books/update/?id={self.book.id}', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")   

    def test_book_delete(self):
        response = self.client.delete(f'/api/books/delete/?id={self.book.id}', format='json')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Book.objects.count(), 0)