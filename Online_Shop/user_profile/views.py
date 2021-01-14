from django.shortcuts import render, redirect
from databaseHandler import search_item
from . import forms

def logged(request):
    return render(request, 'user_profile/logged_user_base.html')


def render_search_site(request,data):
    resolution_options = search_item.get_all_resolution()
    return render(request, 'user_profile/search.html',{'data':data,'resolutions':resolution_options})

def search_items(request):
    searching_item = request.GET.get('search')
    if '+' in searching_item:
        searching_item = searching_item.replace('+',' ')
    data = search_item.search(searching_item)
    return render_search_site(request,data)

def filter_items(request):
    data = search_item.filter(request.GET)
    return render_search_site(request,data)

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