from django import forms


class Add_Post(forms.Form):
    is_boast = forms.BooleanField(required=False)
    contents = forms.CharField(max_length=280, required=True)

