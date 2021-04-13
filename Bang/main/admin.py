from django.contrib import admin
from .models import School, Bar, Party, Menu


class MainAdmin(admin.ModelAdmin):
    list_display = ["id", "text"]


admin.site.register(School, MainAdmin)
admin.site.register(Party, MainAdmin)
admin.site.register(Bar, MainAdmin)
admin.site.register(Menu, MainAdmin)
