import psycopg2
from Online_Shop import settings

def login(login_data):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    postgreSQL_select_Query = "SELECT login,haslo FROM project.klient WHERE login = \'{}\'".format(login_data['login'])
    cur.execute(postgreSQL_select_Query)
    mobile_records = cur.fetchone() 
    user_type = 'client'
    if mobile_records is None:
        postgreSQL_select_Query_stuff = "SELECT login,haslo FROM project.pracownik WHERE login = \'{}\'".format(login_data['login'])
        cur.execute(postgreSQL_select_Query_stuff)
        mobile_records = cur.fetchone() 
        user_type = 'stuff'
        if mobile_records is None:
            cur.close()
            con.close()
            return [False,'Nie ma takiego uzytkownika !']
        else:
            if mobile_records[1] == login_data['password']:
                cur.close()
                con.close()
                return [True,'Autoryzacja pomyslna !',user_type]
            else:
                cur.close()
                con.close()
                return [False,'Zle haslo !']

    else:
        if mobile_records[1] == login_data['password']:
            cur.close()
            con.close()
            return [True,'Autoryzacja pomyslna !',user_type]
        else:
            cur.close()
            con.close()
            return [False,'Zle haslo !']

        
def get_user_id(login_data):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    postgreSQL_select_Query = "SELECT id_klient FROM project.klient WHERE login = \'{}\'".format(login_data['login'])
    cur.execute(postgreSQL_select_Query)
    mobile_records = cur.fetchone() 
    cur.close()
    con.close()
    return mobile_records[0]

def get_staff_id(login_data):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    postgreSQL_select_Query = "SELECT id_pracownik FROM project.pracownik WHERE login = \'{}\'".format(login_data['login'])
    cur.execute(postgreSQL_select_Query)
    mobile_records = cur.fetchone() 
    cur.close()
    con.close()
    return mobile_records[0]
    