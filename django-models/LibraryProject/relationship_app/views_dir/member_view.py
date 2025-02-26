from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda user: user.is_authenticated and user.profile.role == "Member")
def member(request):
    return render(request, "relationship_app/member_view.html")