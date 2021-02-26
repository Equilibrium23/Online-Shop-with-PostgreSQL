from django.shortcuts import render,redirect
from . import forms
from databaseHandler.user import User

def register(request):
    if request.method == 'POST':
        form = forms.registerForm(request.POST)
        if form.is_valid():
            user = User()
            user.register(form.cleaned_data)
            return redirect('login')
    else:
        form = forms.registerForm()
    return render(request, 'register_and_login/register.html', {'form':form,'title':'register'})

def login(request):
    if request.method == 'POST':
        form = forms.loginForm(request.POST)
        if form.is_valid():
            user = User()
            status = user.login(form.cleaned_data)
            if status[0] == True:
                set_session(request,form.cleaned_data)
                if form.cleaned_data['is_staff_member'] == True:
                    return redirect('admin_home')
                else:
                    return redirect('logged')
            else:
                form = forms.loginForm()
                return render(request,'register_and_login/login.html',{'form':form,'title':'login','fail':True})
    else:
        form = forms.loginForm()
    return render(request, 'register_and_login/login.html', {'form':form,'title':'login'})

def set_session(request, login_data):
    user = User()
    if login_data['is_staff_member'] == True:
        user_id = user.get_staff_id(login_data)
    else:
        user_id = user.get_client_id(login_data)
    request.session['user_id'] = user_id



