from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from users.models import User


class UserLoginForm(AuthenticationForm):
    error_messages = {
        "invalid_login": (
            "Будь ласка, введіть правильну електронну пошту або пароль. Зверніть увагу, що обидва поля чутливі до регістру."
        ),
        "inactive": ("Цей обліковий запис неактивний."),
    }

    class Meta():
        model = User
        fields = ['username','password']
    
    username = forms.CharField()
    password = forms.CharField()


class UserRegistrationForm(UserCreationForm):
    class Meta():
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class ProfileForm(UserChangeForm):
    class Meta():
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
        )
        image = forms.ImageField(required=False)
        first_name = forms.CharField()
        last_name = forms.CharField()
