from django import forms

class AccountDetailsForm(forms.Form):
    street = forms.CharField(label = 'ulica', max_length=100)
    miasto = forms.CharField(label = 'miasto', max_length=100)
    postcode = forms.CharField(label = 'kod pocztowy', max_length=100)
    home = forms.IntegerField(label = 'nr domu', max_value=999, min_value = 1)
    flat = forms.IntegerField(label = 'nr mieszkania', max_value=999, min_value = 1)

class OpinionForm(forms.Form):
    opinion = forms.CharField(label = 'opinia', max_length=1000)
    CHOICES= (
            ('1','1'),
            ('2','2'),
            ('3','3'),
            ('3','4'),
            ('3','5'),
            )
    grade = forms.ChoiceField(label = 'ocena', widget=forms.Select, choices=CHOICES)
    hidden_input = forms.CharField(widget=forms.HiddenInput(), initial="0")