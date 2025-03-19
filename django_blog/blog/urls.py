from django.urls import path
from .views import (
    RegisterView,
    Profile,
    home,
    PostListView,
    PostDetailView,
    PostCreateView,
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('accounts/register/', RegisterView, name="register"),
    path('accounts/login/', LoginView.as_view(template_name='blog/login.html'), name="login"),
    path('accounts/logout/', LogoutView.as_view(template_name='blog/logout.html'), name="logout"),
    path('accounts/profile/', Profile, name="profile"),
    path('home/', home, name="home"),
    path('posts/', PostListView.as_view(), name="post_list"),
    path('posts/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('posts/new/', PostCreateView.as_view(), name='post_create')
]