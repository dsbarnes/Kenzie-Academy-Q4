from django import forms
from django.forms import ModelForm
from .models import Custom_User


class Login_Form(forms.Form):
    username = forms.CharField(max_length=42)
    password = forms.CharField(max_length=42)


class Signup_Form(ModelForm):
    class Meta:
        model = Custom_User
        fields = ['email', 'username', 'first_name', 'last_name', 'password']


class Deposit_Form(forms.Form):
    deposit = forms.DecimalField(decimal_places=2, max_digits=8)


class Withdraw_Form(forms.Form):
    withdraw = forms.DecimalField(decimal_places=2, max_digits=8)


class Search_Form(forms.Form):
    ticker = forms.CharField(max_length=5)

