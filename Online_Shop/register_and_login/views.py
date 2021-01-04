from django.shortcuts import render,redirect
from . import forms
from databaseHandler import login as database_login 
from databaseHandler import register as database_register 

def login(request):
    if request.method == 'POST':
        form = forms.loginForm(request.POST)
        if form.is_valid():
            status = database_login.login(form.cleaned_data)
            if status[0] == True:
                return redirect('profile')
            else:
                return render(request,'register_and_login/done.html',{'response' : status})
    else:
        form = forms.loginForm()
    return render(request, 'register_and_login/login.html', {'form':form,'title':'login'})

def register(request):
    if request.method == 'POST':
        form = forms.registerForm(request.POST)
        if form.is_valid():
            database_register.register(form.cleaned_data)
            return render(request,'register_and_login/done.html')
    else:
        form = forms.registerForm()
    return render(request, 'register_and_login/register.html', {'form':form,'title':'register'})