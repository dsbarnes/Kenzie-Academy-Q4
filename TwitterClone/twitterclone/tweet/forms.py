from django import forms


class Add_Tweet(forms.Form):
    body = forms.CharField(max_length=280, required=True, widget=forms.Textarea)