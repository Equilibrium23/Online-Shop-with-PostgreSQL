import psycopg2
from Online_Shop import settings

def register(register_data):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    cur.execute("INSERT INTO project.klient VALUES({},\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');".format('DEFAULT','normal',register_data['name'],register_data['surname'],register_data['login'],register_data['email'],register_data['password']))
    con.commit()
    cur.close()
    con.close()