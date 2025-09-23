from rest_framework.test import APITestCase
from .models import Book, Author
from rest_framework import status
from django.contrib.auth.models import User

class BookModelTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,
            publication_year=2023
        )
        self.list_url = '/api/books/list/'
        self.detail_url = f'/api/books/{self.book.id}/detail/'
    
    def test_book_creation(self):
        # Login required for creating books
        self.client.login(username='testuser', password='testpass')
        new_author = Author.objects.create(name="New Author")
        data = {
            "title": "New Book",
            "author": new_author.id,
            "publication_year": 2024
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
        # Login required for updating books
        self.client.login(username='testuser', password='testpass')
        updated_author = Author.objects.create(name="Updated Author")
        data = {
            "title": "Updated Book",
            "author": updated_author.id,
            "publication_year": 2025
        }
        # Update view uses query parameter, not URL parameter
        response = self.client.put(f'/api/books/update/?id={self.book.id}', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")   

    def test_book_delete(self):
        # Login required for deleting books
        self.client.login(username='testuser', password='testpass')
        # Delete view uses query parameter, not URL parameter
        response = self.client.delete(f'/api/books/delete/?id={self.book.id}', format='json')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Book.objects.count(), 0)