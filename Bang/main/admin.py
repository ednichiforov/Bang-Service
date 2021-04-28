from django.contrib import admin
from .models import School, Bar, Party, About


@admin.register(School, Bar, About)
class MainInfo(admin.ModelAdmin):
    list_display = ["text"]


@admin.register(Party)
class AboutInfo(admin.ModelAdmin):
    list_display = ["text", "picture"]
