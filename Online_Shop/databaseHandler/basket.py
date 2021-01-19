import psycopg2
from Online_Shop import settings
import datetime 

def add_monitor_to_user_basket(request,monitor_id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    cur.execute("SELECT cena FROM project.monitor WHERE id_monitor = {}".format(monitor_id))
    price = cur.fetchone()[0]

    cur.execute("SELECT cena,ilosc FROM project.koszyk WHERE id_uzytkownik = {} AND id_monitor = {}".format(request.session['user_id'],monitor_id))
    mobile_records = cur.fetchone()
    if mobile_records is not None :
        cur.execute("UPDATE project.koszyk SET ilosc = {}, cena = {} WHERE id_uzytkownik = {} AND id_monitor = {} ".format(mobile_records[1]+1,mobile_records[0]+price,request.session['user_id'],monitor_id))
    else:
        cur.execute("INSERT INTO project.koszyk VALUES({},{},{},{},{});".format('DEFAULT',request.session['user_id'],monitor_id,price,'DEFAULT'))

    con.commit()
    cur.close()
    con.close()

def get_user_basket(user_id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    cur.execute("SELECT * FROM pobierz_koszyk({})".format(user_id))
    mobile_records = cur.fetchall()
    basket_sum = 0
    for row in mobile_records:
        basket_sum += row[3]
    mobile_records.append(basket_sum) 
    cur.close()
    con.close()
    return mobile_records

def get_delivery_types():
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    cur.execute("SELECT pobierz_typy_dostawy();")
    mobile_records = cur.fetchall()
    cur.close()
    con.close()
    return mobile_records

def delete_item_from_basket(name,user_id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    delete_query = '''DELETE FROM project.koszyk
                    WHERE id IN (
                    SELECT id FROM
                    project.koszyk WHERE id_uzytkownik={} AND
                    id_monitor = (SELECT id_monitor from project.monitor WHERE nazwa = \'{}\' )
                    LIMIT 1
                    ) '''.format(user_id,name)
    cur.execute(delete_query)
    con.commit()
    cur.close()
    con.close()

def add_order(user_id,delivery_id,suma):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    query = '''SELECT utworz_zamowienie({},{},{},\'{}\',\'{}\');'''.format(user_id,delivery_id,suma,str(datetime.datetime.now()),"W trakcie realizacji")
    cur.execute(query)
    con.commit()
    cur.close()
    con.close()

def delete_all_from_basket(user_id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    delete_query = '''DELETE FROM project.koszyk
                    WHERE id_uzytkownik = {}'''.format(user_id)
    cur.execute(delete_query)
    con.commit()
    cur.close()
    con.close()

def get_user_orders(user_id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    delete_query = '''SELECT c.nazwa,a.id_monitor,a.ilosc,a.id_zamowienie,b.data_zlozenia FROM project.monitor c,project.szczegoly_zamowienia a, project.zamowienie b WHERE b.id_zamowienie = a.id_zamowienie and b.id_uzytkownika = {} and c.id_monitor = a.id_monitor;'''.format(user_id)
    cur.execute(delete_query)
    mobile_records = cur.fetchall()
    result = {}
    for record in mobile_records:
        result.update({record[3]:[]})
    for record in mobile_records:
        result[record[3]].append([record[0],record[1],record[2],str(record[4])])
    print(result)
    cur.close()
    con.close()
    return result
    
