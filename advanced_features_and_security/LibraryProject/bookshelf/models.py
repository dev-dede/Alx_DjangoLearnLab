from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(default=2000)

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"

class CustomUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, profile_photo, password=None):
        if not email:
            raise ValueError("Please enter an email")
        if not date_of_birth:
            raise ValueError("Please enter your date of birth")
        if not profile_photo:
            raise ValueError("Please add a profile photo")
        
        email = self.normalize_email(email)
        user = self.model(email=email, date_of_birth=date_of_birth, profile_photo=profile_photo)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, date_of_birth, profile_photo, password=None):
        user = self.create_user(email, date_of_birth, profile_photo, password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["date_of_birth", "profile_photo"]

    objects = CustomUserManager()