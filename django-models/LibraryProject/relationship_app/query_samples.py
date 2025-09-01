from .models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return Book.objects.none()
    
def get_librarians_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian_set.all()