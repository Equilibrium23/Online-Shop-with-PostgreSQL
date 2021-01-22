import psycopg2
from Online_Shop import settings

tables = ['pracownik','adres','klient','zwrot','szczegoly_zwrotu','ocena','typ_dostawy','zamowienie','szczegoly_zamowienia','monitor','producent','galeria','koszyk']

def get_column_names(cur):
    query_db = ['SELECT * FROM project.{} LIMIT 0;'.format(table) for table in tables]
    result = {}
    for i in range(len(tables)):
        cur.execute(query_db[i])
        table_data = [desc[0] for desc in cur.description]
        result[tables[i]] = table_data
    return result

def select_base():
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    query_db = ['SELECT * FROM project.{};'.format(table) for table in tables]
    column_names = get_column_names(cur)
    result = {}
    for i in range(len(tables)):
        cur.execute(query_db[i])
        table_data = cur.fetchall()
        result[tables[i]] = [column_names[tables[i]],table_data]
    cur.close()
    con.close()
    return result