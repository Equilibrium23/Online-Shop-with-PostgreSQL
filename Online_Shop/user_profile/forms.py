from django import forms

class AccountDetailsForm(forms.Form):
    street = forms.CharField(label = 'ulica', max_length=100)
    miasto = forms.CharField(label = 'miasto', max_length=100)
    postcode = forms.CharField(label = 'kod pocztowy', max_length=100)
    home = forms.IntegerField(label = 'nr domu', max_value=999, min_value = 1)
    flat = forms.IntegerField(label = 'nr mieszkania', max_value=999, min_value = 1)