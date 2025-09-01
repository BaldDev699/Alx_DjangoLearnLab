from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def list_books (request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

class LoginView(CreateView):
    model = User
    template_name = 'relationship_app/login.html'

class LogoutView(CreateView):
    model = User
    template_name = 'relationship_app/logout.html'

@user_passes_test(lambda u: u.is_superuser)
def admin_view(request):
    return render(request, 'relationship_app/admin.html')