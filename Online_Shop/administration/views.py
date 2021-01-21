from django.shortcuts import render,redirect
from databaseHandler import select_base
from .forms import DeleteForm
from .forms import InsertDostawa,InsertMonitor,InsertPracownik,InsertProducent,InsertZdjecie
from .forms import AlterCenaDostawy,AlterCenaMonitora,AlterZamowienie,AlterZwrot
from databaseHandler import admin_insert,admin_alter,admin_delete

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
    elif resource == 'zdjecie':
        form = InsertZdjecie
        if request.method == 'POST':
            form = InsertZdjecie(request.POST)
            if form.is_valid():
                admin_insert.insert_zdjecie(form.cleaned_data)
                return redirect('admin_home')
    elif resource == 'dostawa':
        form = InsertDostawa
        if request.method == 'POST':
            form = InsertDostawa(request.POST)
            if form.is_valid():
                admin_insert.insert_dostawa(form.cleaned_data)
                return redirect('admin_home')
    return render(request, 'administration/forms.html', {'form':form,'form_title':['insert',resource]})


def alter_form(request,resource):
    if resource == 'zamowienie':
        form = AlterZamowienie
        if request.method == 'POST':
            form = AlterZamowienie(request.POST)
            if form.is_valid():
                # insert
                return redirect('admin_home')
    elif resource == 'zwrot':
        form = AlterZwrot
        if request.method == 'POST':
            form = AlterZwrot(request.POST)
            if form.is_valid():
                # insert
                return redirect('admin_home')
    elif resource == 'monitor':
        form = AlterCenaMonitora
        if request.method == 'POST':
            form = AlterCenaMonitora(request.POST)
            if form.is_valid():
                # insert
                return redirect('admin_home')
    elif resource == 'dostawa':
        form = AlterCenaDostawy
        if request.method == 'POST':
            form = AlterCenaDostawy(request.POST)
            if form.is_valid():
                # insert
                return redirect('admin_home')
    return render(request, 'administration/forms.html', {'form':form,'form_title':['alter',resource]})

def manage(request):
    method = request.GET.get('method')
    if method == 'select':
        select = select_base.select_base()
        return render(request,'administration/db.html',{'select':select})
    else:
        resource = request.GET.get('resource')
        if method == 'insert':
            return insert_form(request,resource)
        elif method == 'alter':
            return alter_form(request,resource)
        elif method == 'delete':
            return delete_form(request,resource)
    return redirect('opinions')

def logout(request):
    del request.session['staff_id']
    return redirect('login')