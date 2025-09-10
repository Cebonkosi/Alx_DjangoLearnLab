from django.shortcuts import render
from django.views.generic.detail import DetailView  
from .models import Book
from .models import Library  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView, LogoutView

# Function-based view for listing all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view for showing details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # log the user in after registration
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# Login View – using Django’s built-in
class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"


# Logout View – using Django’s built-in
class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"