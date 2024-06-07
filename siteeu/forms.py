from django import forms
from django.core.validators import EmailValidator

class ContactForm(forms.Form):
    nume = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    mesaj = forms.CharField(widget=forms.Textarea, required=True)
    nr_telefon = forms.CharField(max_length=15 ,required=True)