from django import forms
from . import models


class LoginForm(forms.ModelForm):
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)

    class Meta:
        model = models.Accounts
        fields = ["phone_number", "password"]
