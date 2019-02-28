from django import forms
from django.core import validators
import re

class Sign_up(forms.Form):
    name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=25)
    mobile_number = forms.CharField(max_length=10)
    email = forms.CharField(max_length=60)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=20)
    repeat_password = forms.CharField(widget=forms.PasswordInput(), max_length=20)

class Login(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=20)

