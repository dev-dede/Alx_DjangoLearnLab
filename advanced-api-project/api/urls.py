from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)
from rest_framework.authtoken import views

urlpatterns = [
    path('books/', BookListView.as_view(), name="Book-list"),
    path('books/<int:pk>/', BookDetailView.as_view(), name="Book-detail"),
    path('books/create/', BookCreateView.as_view(), name="Book-create"),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name="Book-update"),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name="Book-delete"),
    path('token-auth/', views.obtain_auth_token)
]