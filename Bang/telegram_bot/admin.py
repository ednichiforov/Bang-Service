from django.contrib import admin
from .models import UsersStartedConv, UserActionLog


@admin.register(UsersStartedConv)
class MainInfo(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "username", "user_id", "is_bot", "created_at"]
    search_fields = ('username', 'user_id')


@admin.register(UserActionLog)
class UserActionLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'action', 'created_at']
