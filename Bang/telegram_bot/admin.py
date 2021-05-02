from django.contrib import admin
from .models import UsersStartedConv, PartyUsersForNearestParty, AllPartyUsers
from import_export.admin import ImportExportModelAdmin


@admin.register(UsersStartedConv)
class MainInfo(ImportExportModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "username",
        "user_id",
        "is_bot",
        "created_at",
    ]
    search_fields = ("username", "user_id")


@admin.register(PartyUsersForNearestParty)
class PartyInfo(ImportExportModelAdmin):
    list_display = [
        "user",
        "real_name",
        "real_last_name",
        "number",
        "user_id",
        "created_at",
    ]


@admin.register(AllPartyUsers)
class AllPartiesInfo(ImportExportModelAdmin):
    list_display = [
        "user",
        "real_name",
        "real_last_name",
        "number",
        "user_id",
        "created_at",
    ]
