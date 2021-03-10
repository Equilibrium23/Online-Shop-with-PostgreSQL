from django import forms

class DeleteForm(forms.Form):
    resource_id = forms.IntegerField(label = 'id', max_value=999, min_value = 1)
    hidden_input = forms.CharField(widget=forms.HiddenInput(), initial="")

class InsertPracownik(forms.Form):
    imie = forms.CharField(label = 'imie', max_length=1000)
    haslo = forms.CharField(label = 'haslo', max_length=1000)
    email = forms.EmailField()
    nazwisko = forms.CharField(label = 'nazwisko', max_length=1000)
    login = forms.CharField(label = 'login', max_length=1000)
    data_zatrudnienia = forms.DateField(label = "data_zatrudnienia w formacie Y-M-D" ,input_formats=['%Y-%m-%d'])
    stanowisko = forms.CharField(label = 'stanowisko', max_length=1000)

class InsertMonitor(forms.Form):
    id_producent = forms.IntegerField(label = 'id_producent', max_value=999, min_value = 1)
    nazwa = forms.CharField(label = 'nazwa', max_length=1000)
    cena = forms.FloatField(max_value=99999, min_value=100)
    przekatna_ekranu = forms.FloatField(max_value=99999, min_value=1)
    rozdzielczosc = forms.CharField(label = 'rozdzielczosc', max_length=1000)
    odswiezanie = forms.IntegerField(label = 'odswiezanie', max_value=999, min_value = 1)
    matryca = forms.CharField(label = 'matryca', max_length=1000)
    max_jasnosc = forms.IntegerField(label = 'max_jasnosc', max_value=999, min_value = 1)


class InsertProducent(forms.Form):
    nazwa = forms.CharField(label = 'nazwa', max_length=1000)
    adres = forms.CharField(label = 'adres', max_length=1000)
    nip = forms.CharField(label = 'nip', max_length=1000)
    email = forms.CharField(label = 'email', max_length=1000)
    nr_tel = forms.CharField(label = 'nr_tel', max_length=1000)
    

class InsertZdjecie(forms.Form):
    id_monitor = forms.IntegerField(label = 'id_monitor', max_value=999, min_value = 1)
    nazwa = forms.CharField(label = 'nazwa', max_length=1000)
    data_dodania = forms.DateField(label = "data_dodania w formacie Y-M-D" ,input_formats=['%Y-%m-%d'])
    image = forms.ImageField(label = 'zdjecie')

class InsertDostawa(forms.Form):
    nazwa = forms.CharField(label = 'nazwa', max_length=1000)
    cena = forms.FloatField(max_value=999, min_value=1)
    firma = forms.CharField(label = 'firma', max_length=1000)


class UpdateZamowienie(forms.Form):
        CHOICES =(
            ['Przetwarzanie','Przetwarzanie'],
            ['Oczekiwane na wplate','Oczekiwane na wplate'],
            ['Wyslane','Wyslane'],
            ['Zrealizowane','Zrealizowane'],
        )
        id_zamowienie = forms.IntegerField(label = 'id_zamowienie', max_value=999, min_value = 1)
        status = forms.ChoiceField(label = 'status', widget=forms.Select, choices=CHOICES)


class UpdateZwrot(forms.Form):
        CHOICES =(
            ['Przetwarzanie','Przetwarzanie'],
            ['Zrealizowane','Zrealizowane'],
            ['Zwrot odrzucony','Zwrot odrzucony'],
        )
        id_zwrot = forms.IntegerField(label = 'id_zwrot', max_value=999, min_value = 1)
        status = forms.ChoiceField(label = 'status', widget=forms.Select, choices=CHOICES)

class UpdateCenaMonitora(forms.Form):
        id_monitor = forms.IntegerField(label = 'id_monitor', max_value=999, min_value = 1)
        cena = forms.FloatField(max_value=99999, min_value=100)

class UpdateCenaDostawy(forms.Form):
        id_dostawa = forms.IntegerField(label = 'id_dostawa', max_value=999, min_value = 1)
        cena = forms.FloatField(max_value=99999, min_value=1)