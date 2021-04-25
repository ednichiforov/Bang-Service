from django.contrib import admin
from .models import School, Bar, Party


@admin.register(School, Bar, Party)
class MainInfo(admin.ModelAdmin):
    list_display = ["text"]
