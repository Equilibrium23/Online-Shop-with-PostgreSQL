import psycopg2
from Online_Shop import settings
import datetime 

def add_monitor_to_user_basket(request,monitor_id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    cur.execute("SELECT cena FROM project.monitor WHERE id_monitor = {}".format(monitor_id))
    price = cur.fetchone()[0]
    cur.execute("INSERT INTO project.koszyk VALUES({},{},{},{});".format('DEFAULT',request.session['user_id'],monitor_id,price))
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
    query = '''SELECT utworz_zamowienie({},{},{},{}) '''.format(user_id,delivery_id,suma,str(datetime.datetime.now()).split(" ")[0])
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