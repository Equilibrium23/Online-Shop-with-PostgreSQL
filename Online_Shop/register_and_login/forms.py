from django import forms

class loginForm(forms.Form):
    login = forms.CharField(label = 'login', max_length=100)
    password = forms.CharField(label = 'haslo', max_length=100, widget=forms.PasswordInput())

class registerForm(forms.Form):
    name = forms.CharField(label = 'name', max_length=100)
    surname = forms.CharField(label = 'surname', max_length=100)
    login = forms.CharField(label = 'login', max_length=100)
    email = forms.CharField(label = 'email', max_length=100)
    password = forms.CharField(label = 'password', max_length=100, widget=forms.PasswordInput())
