import pypyodbc
import sys

class SQL():
    
    def __init__(self,database):
        """ Подключаемся к базе данных"""
        self.err_connect = False
        try:
            self.connection = pypyodbc.connect(database)
            self.cursor = self.connection.cursor()
        except pypyodbc.DatabaseError:
            self.err_connect = True
            #print('Error connect data base ')
    
    def import_data(self,mySQLQuery,alEntID):
        """Считываем данные с базы"""
        self.err_connect = False
        try:
            self.cursor.execute(mySQLQuery,(alEntID))
            result = self.cursor.fetchall()
            return result
        except:
            self.err_connect = True

    def close_connect(self):
        """Закрываем соединение"""
        self.connection.close()





