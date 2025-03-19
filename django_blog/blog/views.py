from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def RegisterView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, f"Account created Successfully!")
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'blog/register.html', {'form': form})

@login_required
def Profile(request):
    return render(request, "blog/profile.html")