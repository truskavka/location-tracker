from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import Form

from tracker.models import CustomUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


class LoginForm(Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
