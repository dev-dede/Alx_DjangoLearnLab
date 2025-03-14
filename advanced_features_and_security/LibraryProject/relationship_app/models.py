from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="books")

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_book", "can add book"),
            ("can_change_book", "can change book"),
            ("can_delete_book", "can delete book"),
        ]
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name="libraries")

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member"),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Member")

    def __str__(self):
        return f"{self.user.username} - {self.role}"