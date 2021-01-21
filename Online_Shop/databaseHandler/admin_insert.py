import psycopg2
from Online_Shop import settings

def insert_pracownik(form):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    insert_query = "INSERT INTO project.pracownik VALUES(DEFAULT, \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\');".format( form['imie'], form['nazwisko'], form['email'], form['login'], form['haslo'], form['data_zatrudnienia'], form['stanowisko']  )
    cur.execute(insert_query)
    con.commit()
    cur.close()
    con.close()

def insert_monitor(form):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    insert_query = "INSERT INTO project.monitor VALUES(DEFAULT,{},\'{}\',{},{},\'{}\',{},\'{}\',{});".format( form['id_producent'], form['nazwa'], form['cena'], form['przekatna_ekranu'], form['rozdzielczosc'], form['odswiezanie'], form['matryca'], form['max_jasnosc'] )
    cur.execute(insert_query)
    con.commit()
    cur.close()
    con.close()

def insert_producent(form):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    insert_query = "INSERT INTO project.producent VALUES(DEFAULT,\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');".format( form['nazwa'], form['adres'], form['nip'], form['email'], form['nr_tel'])
    cur.execute(insert_query)
    con.commit()
    cur.close()
    con.close()

def insert_zdjecie(form):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    insert_query = "INSERT INTO project.galeria VALUES(DEFAULT,{},\'{}\',\'{}\');".format( form['id_monitor'], form['nazwa'], form['data_dodania'])
    cur.execute(insert_query)
    con.commit()
    cur.close()
    con.close()

def insert_dostawa(form):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    insert_query = "INSERT INTO project.pracownik VALUES(DEFAULT,\'{}\',{},\'{}\');".format( form['nazwa'], form['cena'], form['firma_obslugujaca'])
    cur.execute(insert_query)
    con.commit()
    cur.close()
    con.close()