from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        
    # username = forms.CharField(
    #     label="Логин",
    #     widget=forms.TextInput(attrs={"autofocus": True,
    #                                 "class": "login_form-control",
    #                                 "placeholder": "Логин"})
    # )
    # password = forms.CharField(
    #     label="Пароль",
    #     widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
    #                                     "class": "login_form-control",
    #                                     "placeholder": "Пароль"})
    # )

