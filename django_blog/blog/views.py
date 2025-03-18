from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib import messages

def RegisterView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Account created Successfully!")
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'blog/register.html', {'form': form})
