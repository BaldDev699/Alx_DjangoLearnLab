from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.user_profile, name='user_profile'),
    path('posts/', views.ListView, name='post_list'),
    path('post/<int:pk>/', views.DetailView, name='post_detail'),
    path('post/new/', views.CreateView, name='post_create'),
    path('post/<int:pk>/edit/', views.UpdateView, name='post_update'),
    path('post/<int:pk>/delete/', views.DeleteView, name='post_delete'),
]