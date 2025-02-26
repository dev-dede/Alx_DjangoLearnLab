from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda user: user.is_authenticated and user.profile.role == "Admin")
def admin(request):
    return render(request, "admin_view.html")