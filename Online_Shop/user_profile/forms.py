from django import forms

class AccountDetailsForm(forms.Form):
    street = forms.CharField(label = 'ulica', max_length=100)
    miasto = forms.CharField(label = 'miasto', max_length=100)
    postcode = forms.CharField(label = 'kod pocztowy', max_length=100)
    home = forms.CharField(label = 'nr domu', max_length=100)
    flat = forms.CharField(label = 'nr mieszkania', max_length=100)