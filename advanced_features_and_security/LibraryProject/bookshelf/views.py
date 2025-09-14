# advanced_features_and_security/bookshelf/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from django.db.models import Q

@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    return HttpResponse("Create book page - only for users with can_create permission")

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return HttpResponse(f"Edit page for {book.title} - only for users with can_edit permission")

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return HttpResponse(f"Delete page for {book.title} - only for users with can_delete permission")

@login_required
@permission_required('bookshelf.view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()

def search_books(request):
    query = request.GET.get("q", "")
    books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    return render(request, "bookshelf/book_list.html", {"books": books, "query": query})