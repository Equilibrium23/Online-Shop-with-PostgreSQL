import psycopg2
from Online_Shop import settings
import datetime 

def add_user_opinion(form,user_id):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    print(form)
    cur.execute("INSERT INTO project.ocena VALUES({},{},{},\'{}\',{});".format('DEFAULT',user_id,form['hidden_input'],form['opinion'],form['grade']))
    con.commit()
    cur.close()
    con.close()