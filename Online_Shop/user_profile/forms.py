from django import forms
from databaseHandler import basket as user_basket

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


deliveries =user_basket.get_delivery_types()
CHOICES =(
        ['1',deliveries[0][0]],
        ['2',deliveries[1][0]],
        ['3',deliveries[2][0]],
)
class ReturnForm(forms.Form):
    reason = forms.CharField(label = 'powod', max_length=1000)
    CHOICES2 = (
            ('1','Reklamacja'),
            ('2','Zwrot bez podania przyczyny'),
            ('3','Rekojmia'),
            )
    return_type = forms.ChoiceField(label = 'typ', widget=forms.Select, choices=CHOICES2)
    delivery_type = forms.ChoiceField(label = 'dostawa', widget=forms.Select, choices=CHOICES)
    hidden_input = forms.CharField(widget=forms.HiddenInput(), initial="0")