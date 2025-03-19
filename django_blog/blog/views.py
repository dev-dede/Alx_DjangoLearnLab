from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog/home.html", context)

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

class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/post_list.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
    def get_success_url(self):
        return reverse_lazy("post_list")
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    def get_success_url(self):
        return reverse_lazy("post_list")

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    def get_success_url(self):
        return reverse_lazy("post_list")