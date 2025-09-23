from django.urls import path
from .views import (
    BookListCreateView, BookDetailView, 
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

urlpatterns = [
    # RESTful endpoints (recommended)
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    
    # Original endpoints for backward compatibility
    path('books/list/', ListView.as_view(), name='book-list'),
    path('books/<int:pk>/detail/', DetailView.as_view(), name='book-detail-old'),
    path('books/create/', CreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', UpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', DeleteView.as_view(), name='book-delete'),
]