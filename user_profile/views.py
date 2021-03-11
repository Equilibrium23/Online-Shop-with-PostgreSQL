from django.shortcuts import render, redirect
from . import forms
from databaseHandler import basket as user_basket
from databaseHandler import profile as user_profile

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
    user_opinions = user_profile.get_user_opinions(request.session['user_id'])
    return render(request, 'user_profile/user_opinions.html',{'user_opinions':user_opinions})

def user_orders(request):
    user_orders = user_basket.get_user_orders(request.session['user_id'])
    return render(request, 'user_profile/user_orders.html',{'user_orders':user_orders})


def render_user_adresses_site(request):
    form = forms.AccountDetailsForm()
    adressess = user_profile.get_account_details( request.session['user_id'])
    return render(request, 'user_profile/account_details.html', {'form':form,'account_details':True,'adressess':adressess})

def user_adress(request):
    if request.method == 'POST':
        form = forms.AccountDetailsForm(request.POST)
        if form.is_valid():
            user_profile.add_account_details( request.session['user_id'],form.cleaned_data)
    return render_user_adresses_site(request)

def set_main_adress(request):
    user_profile.set_adress(request.GET.get('id_uzytkownik'),request.GET.get('id_adress'))
    return redirect("account_details")

def delete_user_adress(request):
    user_profile.delete_adress(request.GET.get('id_uzytkownik'),request.GET.get('id_adress'))
    return redirect("account_details")


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



def return_product(request):
    if request.method == 'POST':
        form = forms.ReturnForm(request.POST)
        if form.is_valid():
            # dodanie zwrotu jest do dopracowania
            user_profile.make_return(form.cleaned_data,request.session['user_id'],request.GET.get('zamowienie'))
            return redirect('returns')
    else:
        form = forms.ReturnForm()
        form.fields["hidden_input"].initial = request.GET.get('produkt')
    return render(request, 'user_profile/return.html', {'form':form,'return':True})

def logout(request):
    try:
        del request.session['user_id']
        del request.session['redirect']
    except KeyError:
        pass
    return redirect('login')

def show_return_products(request):
    returns = user_profile.get_user_returns(request.session['user_id'])
    return render(request,'user_profile/returns.html',{'returns':returns,'user_opinions':True})