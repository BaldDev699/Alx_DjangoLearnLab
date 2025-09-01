from .models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return author.book_set.all()
    except Author.DoesNotExist:
        return Book.objects.none()

def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return Book.objects.none()