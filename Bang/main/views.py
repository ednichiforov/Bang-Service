from django.shortcuts import render


def general(request):
    return render(request, 'main/general.html')


def school(request):
    return render(request, 'main/school.html')


def party(request):
    return render(request, 'main/party.html')


def bar(request):
    return render(request, 'main/bar.html')


def menu(request):
    return render(request, 'main/menu.html')


def excel(request):
    return render(request, 'main/excel.html')


def users(request):
    return render(request, 'main/users.html')
