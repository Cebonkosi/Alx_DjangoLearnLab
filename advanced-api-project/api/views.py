from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
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

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # ✅ Filtering, Searching, Ordering Setup
    filter_backends = [
        DjangoFilterBackend,      # Filtering
        filters.SearchFilter,     # Searching
        filters.OrderingFilter    # Ordering
    ]

    # ✅ Filtering capabilities
    filterset_fields = ['title', 'author', 'publication_year']

    # ✅ Search functionality
    search_fields = ['title', 'author__name']

    # ✅ Ordering setup
    ordering_fields = ['title', 'publication_year']

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


