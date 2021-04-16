from django.contrib import admin
from .models import School, Bar, Party, Menu


@admin.register(School, Bar, Party, Menu)
class MainInfo(admin.ModelAdmin):
    list_display = ["text"]
