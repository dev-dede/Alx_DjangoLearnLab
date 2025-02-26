from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Author, Librarian, Book

from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "relationship_app/register.html"
    success_url = reverse_lazy("login")

#register = RegisterView.as_view()
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm

# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("login")
#     else:
#         form = UserCreationForm()
#     return render(request, "relationship_app/register.html", {"form": form})


# class LoginView(LoginView):
#     template_name = "relationship_app/login.html"

# class LogoutView(LogoutView):
#     template_name = "relationship_app/logout.html"