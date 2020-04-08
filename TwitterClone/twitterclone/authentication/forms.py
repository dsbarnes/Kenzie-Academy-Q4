from django import forms


class Login_Form(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)


class Signup_Form(forms.Form):
    username = forms.CharField(max_length=50)
    display_name=forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)