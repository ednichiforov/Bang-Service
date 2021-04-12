from django.shortcuts import render
from .models import *


def general(request):
    return render(request, 'main/general.html')


def school(request):
    text = School.objects.all()
    return render(request, 'main/school.html', {"text": text})


def party(request):
    text = Party.objects.all()
    return render(request, 'main/party.html', {"text": text})


def bar(request):
    text = Bar.objects.all()
    return render(request, 'main/bar.html', {"text": text})


def menu(request):
    text = Menu.objects.all()
    return render(request, 'main/menu.html', {"text": text})


def excel(request):
    pass
    return render(request, 'main/excel.html')


def users(request):
    return render(request, 'main/users.html')
