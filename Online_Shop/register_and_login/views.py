from django.shortcuts import render,redirect
from . import forms
from databaseHandler import login as database_login 
from databaseHandler import login as database_login 
from databaseHandler import register as database_register 

def set_user_session(request, login_data):
    user_id = database_login.get_user_id(login_data)
    request.session['user_id'] = user_id

def set_staff_session(request,login_data):
    staff_id = database_login.get_staff_id(login_data)
    request.session['staff_id'] = staff_id

def login(request):
    if request.method == 'POST':
        form = forms.loginForm(request.POST)
        if form.is_valid():
            status = database_login.login(form.cleaned_data)
            if status[0] == True:
                if status[2] == 'stuff':
                    set_staff_session(request,form.cleaned_data)
                    return redirect('administration')
                else:
                    set_user_session(request,form.cleaned_data)
                    return redirect('logged')
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
            return redirect('login')
    else:
        form = forms.registerForm()
    return render(request, 'register_and_login/register.html', {'form':form,'title':'register'})