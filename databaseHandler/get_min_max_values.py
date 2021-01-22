import psycopg2
from Online_Shop import settings

def get_min_max_values():
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cursor = con.cursor()
    columns = ["cena","przekatna_ekranu","odswiezanie","max_jasnosc"]
    min_max_data = {"cena":[],"przekatna_ekranu":[],"rozdzielczosc":[],"odswiezanie":[],"max_jasnosc":[]}
    for column in columns:
        postgreSQL_select_Query_MAX = "SELECT MAX({}) FROM project.monitor".format(column)
        postgreSQL_select_Query_MIN = "SELECT MIN({}) FROM project.monitor".format(column)
        cursor.execute(postgreSQL_select_Query_MIN)
        mobile_records = cursor.fetchone()
        min_max_data[column].append(mobile_records[0])
        cursor.execute(postgreSQL_select_Query_MAX)
        mobile_records = cursor.fetchone()
        min_max_data[column].append(mobile_records[0])
    return min_max_data