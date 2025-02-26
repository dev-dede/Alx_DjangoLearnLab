from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from .views import RegisterView
from .views import LoginView
from .views import LogoutView
from .views_dir.admin_view import admin
from .views_dir.librarian_view import librarian
from .views_dir.member_view import member
from . import views

urlpatterns = [
     path("libraries/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
     path("books/", list_books, name="book-list"),
     #path('register/', views.register, name='register'),
     path('register/', RegisterView.as_view(), name='register'),
     path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
     path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
     path('admin/', admin, name='admin_dashboard'),
     path('librarian/', librarian, name='librarian_dashboard'),
     path('member/', member, name='member_dashboard'),
]