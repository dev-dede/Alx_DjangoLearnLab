from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
# from .views import LibraryDetailView
# from .views import list_books
# from .views import RegisterView
urlpatterns = [
     path("libraries/<int:pk>/", views.LibraryDetailView.as_view(), name="library-detail"),
     path("books/", views.list_books, name="book-list"),
     path('books/add_book/', views.add_book, name='add_book'),
     path('books/edit_book/<int:pk>/', views.change_book, name='change_book'),
     path('books/delete_book/<int:pk>/', views.delete_book, name='delete_book'),
     #path('register/', views.register, name='register'),
     path('register/', views.RegisterView.as_view(), name='register'),
     path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
     path('logout/', LogoutView.as_view(template_name='accounts/logout.html', next_page="/admin/"), name='logout'),
     path('admin/', views.admin_view, name='admin_view'),
     path('librarian/', views.librarian_view, name='librarian_view'),
     path('member/', views.member_view, name='member_view'),
]