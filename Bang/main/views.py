from django.shortcuts import render
from .models import School, Party, Bar
from telegram_bot.models import PartyUsers


def general(request):
    return render(request, 'main/index.html')


def school(request):
    text = School.objects.all()
    return render(request, 'main/school.html', {"text": text})


def party(request):
    text = Party.objects.all()
    return render(request, 'main/party.html', {"text": text})


def bar(request):
    text = Bar.objects.all()
    return render(request, 'main/bar.html', {"text": text})


def users(request, user_id):
    PartyUsers.objects.get(user_id=user_id)
    return render(request, 'main/users.html')
