from django import forms
from . import models


class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)

class RegisterAccount(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    class Meta:
        model = models.Accounts
        fields = ('first_name','last_name',"department",'division','phone_number',"password","is_staff")

    def save(self, commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()
        return user

