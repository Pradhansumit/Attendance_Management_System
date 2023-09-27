from django import forms
from . import models


class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)
