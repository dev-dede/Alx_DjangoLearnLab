from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="post")

    def __str__(self):
        return f'{self.title} by {self.author}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    bio = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'
    
