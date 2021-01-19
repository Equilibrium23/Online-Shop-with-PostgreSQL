from django.shortcuts import render, redirect
from . import forms
from databaseHandler import basket as user_basket
from databaseHandler import profile as user_profile

def logged(request):
    return render(request, 'user_profile/logged_user_base.html')

def profile(request):
    return render(request, 'user_profile/profile.html')

def basket(request):
    if len(request.GET) > 0:
        user_basket.delete_item_from_basket(request.GET.get("name"),request.session['user_id'])
    basket = user_basket.get_user_basket(request.session['user_id'])
    if len(basket) == 1:
        basket[0] = "Nie masz nic w koszyku !" 
        return render(request, 'user_profile/empty_basket.html',{'koszyk':basket})

    delivery = user_basket.get_delivery_types()
    return render(request, 'user_profile/basket.html',{'koszyk':basket[:-1],'sum':basket[-1],'dostawa':delivery})

def user_opinions(request):
    return render(request, 'user_profile/user_opinions.html',{'user_opinions':True})

def user_orders(request):
    user_orders = user_basket.get_user_orders(request.session['user_id'])
    return render(request, 'user_profile/user_orders.html',{'user_orders':user_orders})

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
    user_basket.add_monitor_to_user_basket(request,monitor_id)
    return redirect(request.session['redirect'])

def make_order(request):
    user_basket.add_order(request.session['user_id'],request.POST.get("delivery"),request.POST.get("suma"))
    user_basket.delete_all_from_basket(request.session['user_id'])
    return redirect('profile')

def add_opinion(request):
    if request.method == 'POST':
        form = forms.OpinionForm(request.POST)
        if form.is_valid():
            user_profile.add_user_opinion(form.cleaned_data,request.session['user_id'])
            return redirect('opinions')
    else:
        form = forms.OpinionForm()
        form.fields["hidden_input"].initial = request.GET.get('produkt')
    return render(request, 'user_profile/add_opinion.html', {'form':form,'add_opinion':True})