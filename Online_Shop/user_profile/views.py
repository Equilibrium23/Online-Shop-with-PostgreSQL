from django.shortcuts import render, redirect
from . import forms
from databaseHandler import basket

def logged(request):
    return render(request, 'user_profile/logged_user_base.html')

def profile(request):
    return render(request, 'user_profile/profile.html')

def user_opinions(request):
    return render(request, 'user_profile/user_opinions.html',{'user_opinions':True})

def user_orders(request):
    return render(request, 'user_profile/user_orders.html',{'user_orders':True})

def account_details(request):
    if request.method == 'POST':
        form = forms.AccountDetailsForm(request.POST)
        if form.is_valid():
            ### to do -> insert data
            return redirect('profile')
    else:
        form = forms.AccountDetailsForm()
    return render(request, 'user_profile/account_details.html', {'form':form,'account_details':True})


def add_item_to_basket(request,monitor_id):
    basket.add_monitor_to_user_basket(request,monitor_id)
    return redirect(request.session['redirect'])