from .models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)

def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return Book.objects.none()
    
def get_librarians_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except Library.DoesNotExist:
        return None