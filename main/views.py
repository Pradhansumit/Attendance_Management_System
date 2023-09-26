from django.shortcuts import render
from django.views.generic import FormView
from . import forms

# view to display the homepage...


class Index(FormView):
    form_class = forms.LoginForm
    template_name = "main/index.html"
