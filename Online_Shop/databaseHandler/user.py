from Online_Shop import settings
import psycopg2

class User:
    def __init__(self):
        self.connection = psycopg2.connect(database=settings.DATABASE['NAME'], user=settings.DATABASE['USER'], password=settings.DATABASE['PASSWORD'], host=settings.DATABASE['HOST'], port=settings.DATABASE['PORT'])

    def __del__(self):
        self.connection.close()

    def register(self,register_data):
        cursor = self.connection.cursor()
        register_query = "INSERT INTO project.klient VALUES({},\'{}\',\'{}\',\'{}\',\'{}\',\'{}\');".format('DEFAULT',register_data['name'],register_data['surname'],register_data['login'],register_data['password'],register_data['email'])
        try:
            cursor.execute(register_query)
            status = "OK"    
        except:
            status = "ERROR"    
        self.connection.commit()
        cursor.close()
        print("XD")
        return status

    def check_user_password(self,user_record,password):
        if user_record[1] == password:
            return [True,'Autoryzacja pomyslna !']
        else:
            return [False,'Zle haslo !']

    def login(self,login_data):
        cursor = self.connection.cursor()
        if  login_data['is_staff_member'] is True:
            get_user_query = "SELECT login,haslo FROM project.pracownik WHERE login = \'{}\'".format(login_data['login'])
            user_type = 'staff'
        else:
            get_user_query = "SELECT login,haslo FROM project.klient WHERE login = \'{}\'".format(login_data['login'])
            user_type = 'client'

        cursor.execute(get_user_query)
        user_record = cursor.fetchone() 

        if user_record is None:
            login_status = [False,'Nie ma takiego uzytkownika !']
        else:
            login_status = self.check_user_password(user_record,login_data['password'])
        login_status.append(user_type)
        cursor.close()
        return login_status
    
    def get_client_id(self,login_data):
        cursor = self.connection.cursor()
        get_client_id_query = "SELECT id_klient FROM project.klient WHERE login = \'{}\'".format(login_data['login'])
        cursor.execute(get_client_id_query)
        client_record = cursor.fetchone() 
        cursor.close()
        return client_record[0]

    def get_staff_id(self,login_data):
        cursor = self.connection.cursor()
        get_staff_member_id_query = "SELECT id_pracownik FROM project.pracownik WHERE login = \'{}\'".format(login_data['login'])
        cursor.execute(get_staff_member_id_query)
        staff_member_record = cursor.fetchone() 
        cursor.close()
        return staff_member_record[0]

    
        

