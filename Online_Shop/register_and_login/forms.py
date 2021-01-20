from django import forms

class loginForm(forms.Form):
    login = forms.CharField(label = 'login', max_length=100)
    password = forms.CharField(label = 'haslo', max_length=100, widget=forms.PasswordInput())

class registerForm(forms.Form):
    name = forms.CharField(label = 'imie', max_length=100)
    surname = forms.CharField(label = 'nazwisko', max_length=100)
    login = forms.CharField(label = 'login', max_length=100)
    email = forms.EmailField(label = 'email')
    password = forms.CharField(label = 'haslo', max_length=100, widget=forms.PasswordInput())
