from django.test import APITestCase
from .models import Book

class BookModelTest(APITestCase):
    def setUp(self):
        Book.objects.create(title="Test Book", author="Author A", published_year=2020)

    def test_book_creation(self):
        book = Book.objects.get(title="Test Book")
        self.assertEqual(book.author, "Author A")
        self.assertEqual(book.published_year, 2020)

    def test_book_update(self):
        book = Book.objects.get(title="Test Book")
        book.author = "Author B"
        book.save()
        updated_book = Book.objects.get(title="Test Book")
        self.assertEqual(updated_book.author, "Author B")

    def test_book_deletion(self):
        book = Book.objects.get(title="Test Book")
        book.delete()
        books = Book.objects.all()
        self.assertEqual(len(books), 0)