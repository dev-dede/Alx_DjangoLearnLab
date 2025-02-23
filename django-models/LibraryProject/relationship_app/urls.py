from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from .views import RegisterView
from .views import UserLoginView
from .views import UserLogoutView

urlpatterns = [
     path("libraries/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
     path("books/", list_books, name="book-list"),
     path('register/', RegisterView.as_view(), name='register'),
     path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
     path('logout/', LogoutView.as_view(), name='logout'),
]