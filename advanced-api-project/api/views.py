from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

"""
BookListView

Features:
- Filtering by title, author, publication_year (e.g. ?title=Python)
- Searching in title or author name (e.g. ?search=John)
- Ordering by title or publication_year (e.g. ?ordering=-publication_year)

Examples:
- /api/books/?search=Django
- /api/books/?author=1&ordering=title
"""

# List all books (Read-only for unauthenticated users)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Anyone can view

 # ✅ Enable filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend,      # For filtering
        filters.SearchFilter,      # For searching
        filters.OrderingFilter     # For ordering
    ]

    # ✅ Filtering options
    filterset_fields = ['title', 'author', 'publication_year']

    # ✅ Search fields (partial match using ?search=term)
    search_fields = ['title', 'author__name']  # Double underscore for foreign key lookup

    # ✅ Ordering options
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering

# Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Create a new book (Restricted to authenticated users)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


