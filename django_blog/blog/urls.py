from django.urls import path
from .views import (
    RegisterView
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('accounts/register/', RegisterView, name="register"),
    path('accounts/login/', LoginView.as_view(template_name='blog/login.html'), name="login"),
    path('accounts/logout/', LogoutView.as_view(template_name='blog/logout.html'), name="logout"),
]