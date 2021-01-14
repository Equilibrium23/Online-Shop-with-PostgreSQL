import psycopg2
from Online_Shop import settings

def add_monitor_to_user_basket(request,monitor_id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    cur.execute("SELECT cena FROM project.monitor WHERE id_monitor = {}".format(monitor_id))
    price = cur.fetchone()[0]
    cur.execute("INSERT INTO project.koszyk VALUES({},{},{},{});".format('DEFAULT',request.session['user_id'],monitor_id,price))
    con.commit()
    cur.close()
    con.close()