import psycopg2
from Online_Shop import settings

def update_zamowienie(form):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    update_query = "UPDATE project.zamowienie SET status_zamowienia = \'{}\' WHERE id_zamowienie = {}".format(form['status'], form['id_zamowienie'])
    cur.execute(update_query)
    con.commit()
    cur.close()
    con.close()

def update_zwrot(form):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    update_query = "UPDATE project.zwrot SET status_zwrotu = \'{}\' WHERE id_zwrot = {}".format(form['status'], form['id_zwrot'])
    cur.execute(update_query)
    con.commit()
    cur.close()
    con.close()

def update_monitor(form):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    update_query = "UPDATE project.monitor SET cena = {} WHERE id_monitor = {}".format(form['cena'], form['id_monitor'])
    cur.execute(update_query)
    con.commit()
    cur.close()
    con.close()

def update_dostawa(form):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    update_query = "UPDATE project.typ_dostawy SET cena_dostawy = {} WHERE id_typu_dostawy = {}".format(form['cena'], form['id_dostawa'])
    cur.execute(update_query)
    con.commit()
    cur.close()
    con.close()

