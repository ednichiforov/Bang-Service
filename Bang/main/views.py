from django.shortcuts import render
from .models import School, Party, Bar, About
from telegram_bot.models import PartyUsersForNearestParty
from django.conf import settings


def general(request):
    bar_text = Bar.objects.only("text").last()
    school_text = School.objects.only("text").last()
    party_text = Party.objects.only("text").last()
    about_text = About.objects.only("text").last()
    picture_name = getattr(Party.objects.last(), "picture")
    media = f"{settings.MEDIA_URL}{picture_name}"
    text_field = {
        "bar_text": bar_text,
        "school_text": school_text,
        "party_text": party_text,
        "about_text": about_text,
        "picture_name": picture_name,
        "media": media,
    }
    return render(request, "main/index.html", text_field)


def users(request, user_id):
    PartyUsersForNearestParty.objects.get(user_id=user_id)
    picture_name = getattr(Party.objects.last(), "picture")
    media = f"{settings.MEDIA_URL}{picture_name}"
    return render(request, "main/users.html", {"media": media})
