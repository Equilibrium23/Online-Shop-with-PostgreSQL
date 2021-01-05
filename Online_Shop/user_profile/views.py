from django.shortcuts import render
from databaseHandler import search_item

def logged(request):
    return render(request, 'user_profile/logged.html')

def search_items(request):
    searching_item = request.GET.get('search')
    if '+' in searching_item:
        searching_item = searching_item.replace('+',' ')
    data = search_item.search(searching_item)
    return render(request, 'user_profile/search.html',{'data':data})

def filter_items(request):
    return render(request, 'user_profile/search.html')
