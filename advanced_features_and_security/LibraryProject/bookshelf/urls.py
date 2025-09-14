# advanced_features_and_security/bookshelf/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.view_books, name='view_books'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]
