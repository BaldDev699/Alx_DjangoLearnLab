from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView

# Create your views here.
def list_books (request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class SignUpView(CreateView):
    model = User
    template_name = 'relationship_app/signup.html'
    form_class = UserCreationForm

class LoginView(CreateView):
    model = User
    template_name = 'relationship_app/login.html'

class LogoutView(CreateView):
    model = User
    template_name = 'relationship_app/logout.html'