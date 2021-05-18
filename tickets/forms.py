from django import forms

class TForm(forms.Form):
    sender = forms.EmailField()