import psycopg2
from Online_Shop import settings


def get_all_resolution():
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cursor = con.cursor()
    postgreSQL_select_Query = "SELECT rozdzielczosc FROM project.monitor"
    cursor.execute(postgreSQL_select_Query)
    mobile_records = cursor.fetchall()
    if mobile_records is None:
        cursor.close()
        con.close()
        return []
    else:
        set_of_resolution = set()
        for row in mobile_records:
            set_of_resolution.add(row[0])
        return set_of_resolution



def create_data_from_fetch(mobile_records,cursor):
    column_names = [column[0] for column in cursor.description]
    cursor.execute("SELECT id_monitora,nazwa_zdjecia FROM project.galeria;")
    temp = cursor.fetchall()
    pictures = {info[0]:info[1] for info in temp}
    data = [{} for _ in range(len(mobile_records))]
    for i in range(len(mobile_records)):
        for j in range(len(mobile_records[i])):
            data[i][column_names[j]] = mobile_records[i][j]
        try:
            data[i]['path'] = pictures[data[i]['id_monitor']]
        except:
            pass
    return data


def search(searching_item):
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    postgreSQL_select_Query = "SELECT * FROM project.monitor WHERE nazwa ILIKE \'%{}%\'".format(searching_item)
    cur.execute(postgreSQL_select_Query)
    mobile_records = cur.fetchall()
    if mobile_records is None:
        cur.close()
        con.close()
        return []
    else:
        data = create_data_from_fetch(mobile_records,cur)
    return data

def filter(data):
    cleanedData  = {a:b for a,b in data.items()}
    checkBoxModel = [] # ok
    checkBoxMatryca = [] # ok
    cena = [] 
    przekatna = []
    rozdzielczosc = []
    odswiezanie = []
    jasnosc = []
    sort = []
    for desc,value in cleanedData.items():
        if value == 'on':
            if desc == 'ips' or desc == 'tn' or desc == 'va':
                checkBoxMatryca.append(desc)
            elif 'x' in desc:
                rozdzielczosc.append(desc)
            else:
                checkBoxModel.append(desc)
        if 'cena' in desc:
            cena.append(value)
        if 'przekatna' in desc:
            przekatna.append(value)
        if 'rozdzielczosc' in desc:
            rozdzielczosc.append(value)
        if 'odswiezanie' in desc:
            odswiezanie.append(value)
        if 'jasnosc' in desc:
            jasnosc.append(value)
        if 'sort' == desc:
            sort.append(value)
    ############################## create rozdzielczosc query ####################
    rozdzielczoscQuery = ""
    if len(rozdzielczosc) > 0:
        rozdzielczoscQuery+= rozdzielczosc[0]
        if len(rozdzielczosc) > 1:
            for x in rozdzielczosc[1:]:
                rozdzielczoscQuery+="|"+x
    print(rozdzielczoscQuery)
    ######################################################################
    ############################## create model query ####################
    modelQuery = ""
    if len(checkBoxModel) > 0:
        modelQuery+= checkBoxModel[0]
        if len(checkBoxModel) > 1:
            for model in checkBoxModel[1:]:
                modelQuery+="|"+model
    ######################################################################
    ############################## create matryca query ####################
    matrycaQuery = ""
    if len(checkBoxMatryca) > 0:
        matrycaQuery+= checkBoxMatryca[0]
        if len(checkBoxMatryca) > 1:
            for matryca in checkBoxMatryca[1:]:
                matrycaQuery+="|"+matryca
    ###################################################################### 
    con = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])
    cur = con.cursor()
    if len(sort) > 0 :
        sort.append(cleanedData["sort_type"])
        postgreSQL_select_Query = '''SELECT * FROM project.monitor
                                    WHERE nazwa ~* \'{}\'
                                    AND matryca ~* \'{}\'
                                    AND rozdzielczosc ~* \'{}\'
                                    AND (cena BETWEEN {} AND {})
                                    AND (przekatna_ekranu BETWEEN {} AND {})
                                    AND (odswiezanie BETWEEN {} AND {})
                                    AND max_jasnosc < {}
                                    ORDER BY {} {}
                                    '''.format(modelQuery,matrycaQuery,rozdzielczoscQuery,cena[0],cena[1],przekatna[0],przekatna[1],odswiezanie[0],odswiezanie[1],jasnosc[0],sort[0],sort[1])
        cur.execute(postgreSQL_select_Query)
        mobile_records = cur.fetchall()
    else:
        postgreSQL_select_Query = '''SELECT * FROM project.monitor
                                    WHERE nazwa ~* \'{}\'
                                    AND matryca ~* \'{}\'
                                    AND rozdzielczosc ~* \'{}\'
                                    AND (cena BETWEEN {} AND {})
                                    AND (przekatna_ekranu BETWEEN {} AND {})
                                    AND (odswiezanie BETWEEN {} AND {})
                                    AND max_jasnosc < {}
                                    '''.format(modelQuery,matrycaQuery,rozdzielczoscQuery,cena[0],cena[1],przekatna[0],przekatna[1],odswiezanie[0],odswiezanie[1],jasnosc[0])
        cur.execute(postgreSQL_select_Query)
        mobile_records = cur.fetchall()
    if mobile_records is None:
        cur.close()
        con.close()
        return []
    else:
        return_data = create_data_from_fetch(mobile_records,cur)
    return return_data