from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # Columns shown in admin list view
    search_fields = ("title", "author")  # Search by title or author
    list_filter = ("publication_year",)  # Filter by publication year
