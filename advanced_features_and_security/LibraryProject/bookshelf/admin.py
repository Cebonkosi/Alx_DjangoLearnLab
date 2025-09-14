# LibraryProject/bookshelf/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    # Define fields to be displayed in the admin list
    list_display = ('email', 'date_of_birth', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')

    # Fieldsets for editing user details
    fieldsets = (
        (None, {'fields': ('email', 'password', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fields used when creating a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'profile_photo', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    search_fields = ('email',)
    ordering = ('email',)


# ✅ Register CustomUser with its admin
admin.site.register(CustomUser, CustomUserAdmin)
