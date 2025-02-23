from django.urls import path
from .views import LibraryDetailView
from .views import list_books

urlpatterns = [
     path("libraries/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
     path("books/", list_books, name="book-list"),
]