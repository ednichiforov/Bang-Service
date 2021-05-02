from django.shortcuts import render
from .models import School, Party, Bar, About
from telegram_bot.models import PartyUsersForNearestParty
from django.conf import settings

try:
    picture_name = getattr(Party.objects.last(), "picture")
except AttributeError:
    picture_name = None

party_picture = f"{settings.MEDIA_URL}{picture_name}"


def general(request):
    bar_text = Bar.objects.only("text").last()
    school_text = School.objects.only("text").last()
    party_text = Party.objects.only("text").last()
    about_text = About.objects.only("text").last()

    db_info = {
        "bar_text": bar_text,
        "school_text": school_text,
        "party_text": party_text,
        "about_text": about_text,
        "party_picture": party_picture,
    }

    return render(request, "main/index.html", db_info)


def users(request, user_id):
    PartyUsersForNearestParty.objects.get(user_id=user_id)
    return render(request, "main/users.html", {"party_picture": party_picture})
