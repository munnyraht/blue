# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import BluecreditUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = BluecreditUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = BluecreditUser
        fields = ('username', 'email')