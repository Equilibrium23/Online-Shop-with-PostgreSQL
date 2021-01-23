from django.shortcuts import render,redirect
from databaseHandler import select_base
from .forms import DeleteForm
from .forms import InsertDostawa,InsertMonitor,InsertPracownik,InsertProducent
from .forms import UpdateCenaDostawy,UpdateCenaMonitora,UpdateZamowienie,UpdateZwrot
from databaseHandler import admin_insert,admin_update,admin_delete

def home(request):
    return render(request,'administration/admin.html')

def delete_form(request,resource):
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            admin_delete.delete(form.cleaned_data)
            return redirect('admin_home')
    else:
        form = DeleteForm()
        form.fields["hidden_input"].initial = resource
    return render(request, 'administration/forms.html', {'form':form,'form_title':['delete',resource]})



def insert_form(request,resource):
    if resource == 'pracownik':
        form = InsertPracownik
        if request.method == 'POST':
            form = InsertPracownik(request.POST)
            if form.is_valid():
                admin_insert.insert_pracownik(form.cleaned_data)
                return redirect('admin_home')
    elif resource == 'monitor':
        form = InsertMonitor
        if request.method == 'POST':
            form = InsertMonitor(request.POST)
            if form.is_valid():
                admin_insert.insert_monitor(form.cleaned_data)
                return redirect('admin_home')
    elif resource == 'producent':
        form = InsertProducent
        if request.method == 'POST':
            form = InsertProducent(request.POST)
            if form.is_valid():
                admin_insert.insert_producent(form.cleaned_data)
                return redirect('admin_home')
    elif resource == 'dostawa':
        form = InsertDostawa
        if request.method == 'POST':
            form = InsertDostawa(request.POST)
            if form.is_valid():
                admin_insert.insert_dostawa(form.cleaned_data)
                return redirect('admin_home')
    return render(request, 'administration/forms.html', {'form':form,'form_title':['insert',resource]})


def update_form(request,resource):
    if resource == 'zamowienie':
        form = UpdateZamowienie
        if request.method == 'POST':
            form = UpdateZamowienie(request.POST)
            if form.is_valid():
                admin_update.update_zamowienie(form.cleaned_data)
                return redirect('admin_home')
    elif resource == 'zwrot':
        form = UpdateZwrot
        if request.method == 'POST':
            form = UpdateZwrot(request.POST)
            if form.is_valid():
                admin_update.update_zwrot(form.cleaned_data)
                return redirect('admin_home')
    elif resource == 'monitor':
        form = UpdateCenaMonitora
        if request.method == 'POST':
            form = UpdateCenaMonitora(request.POST)
            if form.is_valid():
                admin_update.update_monitor(form.cleaned_data)
                return redirect('admin_home')
    elif resource == 'dostawa':
        form = UpdateCenaDostawy
        if request.method == 'POST':
            form = UpdateCenaDostawy(request.POST)
            if form.is_valid():
                admin_update.update_dostawa(form.cleaned_data)
                return redirect('admin_home')
    return render(request, 'administration/forms.html', {'form':form,'form_title':['update',resource]})

def manage(request):
    method = request.GET.get('method')
    if method == 'select':
        select = select_base.select_base()
        return render(request,'administration/db.html',{'select':select})
    else:
        resource = request.GET.get('resource')
        if method == 'insert':
            return insert_form(request,resource)
        elif method == 'update':
            return update_form(request,resource)
        elif method == 'delete':
            return delete_form(request,resource)
    return redirect('admin_home')

def logout(request):
    del request.session['staff_id']
    return redirect('login')