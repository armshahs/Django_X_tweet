from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth.models import User
from .models import UserProfile


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")
