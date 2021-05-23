from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'banned_at',) 
    fieldsets = (
            (None, {'fields': ('banned_at', 'ip',)}),
    ) + UserAdmin.fieldsets