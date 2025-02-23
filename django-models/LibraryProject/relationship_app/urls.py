from django.urls import path
from .views import LibraryDetailView, book_list

urlpatterns = [
     path("libraries/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
     path("books/", book_list, name="book-list"),
]