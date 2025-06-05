from dataclasses import fields
from email.mime import image
from pyexpat import model
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

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


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            # "role",
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    role = forms.ChoiceField(
        label='Роль',
        choices=[
            ('customer', 'Покупатель'),
            ('seller', 'Продавец'),
            ('staff_warehouse', 'Сотрудник склада'),
            ('staff_delivery', 'Сотрудник доставки'),
        ],
        required=True, # Добавьте эту строку, чтобы поле было обязательным для заполнения
    )
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email",
        )
    
    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    
    # image = forms.ImageField(
    #     widget=forms.FileInput(attrs={"class": "form_control-image"}), required=False
    # )
