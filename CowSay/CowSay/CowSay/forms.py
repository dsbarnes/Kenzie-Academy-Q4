from django import forms

class Cow_Say_Form(forms.Form):
    cow_says = forms.CharField(max_length=50)