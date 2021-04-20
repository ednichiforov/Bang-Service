from django.contrib import admin
from .models import School, Bar, Party, Menu


@admin.register(School, Bar, Menu, Party)
class MainInfo(admin.ModelAdmin):
    list_display = ["text"]

