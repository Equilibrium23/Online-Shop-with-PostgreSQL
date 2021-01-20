import psycopg2
from Online_Shop import settings
import datetime 

def add_user_opinion(form,user_id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    cur.execute("INSERT INTO project.ocena VALUES({},{},{},\'{}\',{});".format('DEFAULT',user_id,form['hidden_input'],form['opinion'],form['grade']))
    con.commit()
    cur.close()
    con.close()

def get_user_opinions(user_id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    cur.execute("SELECT m.nazwa,o.tekst_oceny,o.ocena FROM project.ocena o, project.monitor m WHERE o.id_produktu = m.id_monitor and  o.id_autora = {};".format(user_id))
    mobile_records = cur.fetchall()
    cur.close()
    con.close()
    return mobile_records

def get_all_opinions():
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    cur.execute("SELECT * FROM project.ocena;")
    all_rows = cur.fetchall()
    cur.execute("SELECT id_produktu,CAST(sum(ocena) AS FLOAT)/COUNT(*) FROM project.ocena group by id_produktu;")
    details =  cur.fetchall()
    average_grade = { detail[0]:detail[1] for detail in details}
    data = { row[2]:[[],0] for row in all_rows }
    for row in all_rows:
        data[row[2]][0].append(row[3])

    for item,info in data.items():
        info[1]=average_grade[item]

    cur.close()
    con.close()
    return data

def add_account_details(user_id,form):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    cur.execute(''' INSERT INTO project.adres VALUES(DEFAULT,{},\'{}\',\'{}\',\'{}\',{},{}
    )'''.format(user_id, form['street'], form['miasto'], form['postcode'], form['home'], form['flat']))
    con.commit()
    cur.close()
    con.close()

def get_account_details(user_id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    cur.execute("SELECT * FROM project.adres WHERE id_uzytkownik = {};".format(user_id))
    mobile_records = cur.fetchall()
    cur.close()
    con.close()
    return mobile_records

def set_adress(id_uzytkownik,id_adress):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    cur.execute('''UPDATE project.adres
                SET glowny_adres = false WHERE id_uzytkownik = {};
    '''.format(id_uzytkownik))
    con.commit()
    cur.execute('''UPDATE project.adres
                SET glowny_adres = true WHERE id_uzytkownik = {} and id_adres = {};
    '''.format(id_uzytkownik,id_adress))
    con.commit()
    cur.close()
    con.close()

def delete_adress(id_uzytkownik,id_adress):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    cur.execute('''DELETE FROM project.adres *
                WHERE id_uzytkownik = {} and id_adres = {};
    '''.format(id_uzytkownik,id_adress))
    con.commit()
    cur.close()
    con.close()

def make_return(form,id_uzytkownik,id_szczegoly_zamowienia):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    query = '''SELECT project.utworz_zwrot({},{},\'{}\',{},{},\'{}\');'''.format(id_uzytkownik, form['delivery_type'], form['reason'], form['hidden_input'], id_szczegoly_zamowienia, 'xd')
    cur.execute(query)
    con.commit()
    cur.close()
    con.close()