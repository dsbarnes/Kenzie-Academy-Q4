from django import forms
from .models import Author


class Add_Recipe(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=50)
    instructions = forms.CharField(max_length=250)
    time_required = forms.CharField(max_length=5)
    author = forms.ModelChoiceField(queryset=Author.objects.all())


class Add_Author(forms.Form):
    # user_id = ??? perhaps User.objects.something
    name = forms.CharField(max_length=50)
    bio = forms.CharField(max_length=250)

class Login_Form(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

class Signup_Form(forms.Form):
    name = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    bio = forms.CharField(max_length=250)
