from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "bio",
        "profile_picture",
    )

    filter_horizontal = ("followers",)

admin.site.register(CustomUser, CustomUserAdmin)
