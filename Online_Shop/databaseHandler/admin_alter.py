import psycopg2
from Online_Shop import settings

def alter_zamowienie(form):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    alter_query = "ALTER TABLE project.zamowienie SET COLUMN status_zamowienia = \'{}\' WHERE id_zamowienie".format(form['status'], form['id_zamowienie'])
    cur.execute(alter_query)
    con.commit()
    cur.close()
    con.close()