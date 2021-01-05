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
        return []
    else:
        column_names = [column[0] for column in cur.description]
        data = [{} for _ in range(len(column_names))]
        for i in range(len(mobile_records)):
            for j in range(len(mobile_records[i])):
                data[i][column_names[j]] = mobile_records[i][j]
    return data