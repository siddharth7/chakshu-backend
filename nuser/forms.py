from django import forms

class FoundPersonForm(forms.Form):
    name = forms.CharField(max_length=40)
    location = forms.CharField(max_length=40)
    picture = forms.ImageField()