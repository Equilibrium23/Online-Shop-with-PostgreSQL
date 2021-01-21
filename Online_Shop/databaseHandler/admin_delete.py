import psycopg2
from Online_Shop import settings

def delete(form):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    delete_query = "DELETE FROM project.{} * WHERE id_{} = {}".format(form['hidden_input'], form['hidden_input'] ,form['resource_id'])
    cur.execute(delete_query)
    con.commit()
    cur.close()
    con.close()