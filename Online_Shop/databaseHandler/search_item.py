import psycopg2
from Online_Shop import settings

def search(searching_item):
    print(searching_item)
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    postgreSQL_select_Query = "SELECT * FROM project.monitor WHERE nazwa LIKE \'%{}%\'".format(searching_item)
    cur.execute(postgreSQL_select_Query)
    mobile_records = cur.fetchall()
    if mobile_records is None:
        cur.close()
        con.close()
        return [False]
    else:
        data = [x for x in mobile_records]
    return data