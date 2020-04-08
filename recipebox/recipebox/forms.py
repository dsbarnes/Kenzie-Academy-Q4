from django import forms
from recipebox.models import Author


class RecipeAddForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    time_required = forms.CharField(max_length=15)
    instructions = forms.CharField(widget=forms.Textarea)


class RecipeEditForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    time_required = forms.CharField(max_length=15)
    instructions = forms.CharField(widget=forms.Textarea)


class AuthorAddForm(forms.Form):
    name = forms.CharField(max_length=30)
    bio = forms.CharField(widget=forms.Textarea)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    name = forms.CharField(max_length=30)
    bio = forms.CharField(widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
