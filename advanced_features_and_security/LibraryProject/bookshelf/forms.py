# LibraryProject/bookshelf/forms.py
from django import forms
from .models import Book

# Example form for creating/editing books
class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
