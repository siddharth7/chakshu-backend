from django import forms

class FoundPersonForm(forms.Form):
    uploaded_by=forms.CharField(max_length=40)
    name = forms.CharField(max_length=40)
    location = forms.CharField(max_length=40)
    picture = forms.ImageField()