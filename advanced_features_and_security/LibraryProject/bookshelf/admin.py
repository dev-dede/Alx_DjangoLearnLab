from django.contrib import admin
from .models import Book
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('author', 'title')

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'profile_photo', 'date_of_birth', 'is_staff', 'is_superuser')

admin.site.register(CustomUser, CustomUserAdmin)