from django.shortcuts import render,redirect

#logged user home
def home(request):
    return render(request, 'home/home.html')

#logout user home
def start_page(request):
    return render(request,'home/start_page.html',{'title':'start page','option':'home'})