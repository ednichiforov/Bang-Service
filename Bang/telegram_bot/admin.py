from django.contrib import admin
from .models import UsersStartedConv, PartyUsers


@admin.register(UsersStartedConv)
class MainInfo(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "username", "user_id", "is_bot", "created_at"]
    search_fields = ('username', 'user_id')


@admin.register(PartyUsers)
class MainInfo(admin.ModelAdmin):
    list_display = ["user", "real_name", "real_last_name", "number", "user_id"]
