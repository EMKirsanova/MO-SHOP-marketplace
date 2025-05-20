from django.shortcuts import render
from django.http import HttpResponse


def login(request):

    context = {
        'title': 'МО-ШОП — Авторизация',
        'content': '',
    }

    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'МО-ШОП — Регистрация',
        'content': '',
    }

    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'МО-ШОП — Профиль',
        'content': '',
    }

    return render(request, 'users/profile.html', context)


def logout(request):
    ...

