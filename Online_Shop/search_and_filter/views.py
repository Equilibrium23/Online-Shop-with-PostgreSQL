from django.shortcuts import render
from databaseHandler import search_item
from databaseHandler import get_min_max_values

def render_search_site(request,data):
    resolution_options = search_item.get_all_resolution()
    filters_min_max_values = get_min_max_values.get_min_max_values()
    return render(request, 'search_and_filter/search.html',{'data':data,'resolutions':resolution_options,'filters_limits':filters_min_max_values})

def search_items(request):
    searching_item = request.GET.get('search')
    if '+' in searching_item:
        searching_item = searching_item.replace('+',' ')
    data = search_item.search(searching_item)
    return render_search_site(request,data)

def filter_items(request):
    data = search_item.filter(request.GET)
    return render_search_site(request,data)