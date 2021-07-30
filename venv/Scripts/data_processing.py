import data_base
import time
import json
import config


""" Обработка данных полученных от БД """
class Processing():
    def __init__(self,db_data):
        self.db_data = db_data

    def extract_data(self, number_variable):  # Указаваем какой элемент из списка нам требуется извлечь
        listDataElement = []
        for i, j in enumerate(self.db_data):
            listDataElement.insert(i, j[number_variable - 1])
        return listDataElement

""" Создание списка с номерами ID до 1000 """
def extractListMinNumber(list):
    listMinNumber = []
    for i in list:
        if i < 1000:
            listMinNumber.append(i)
    return listMinNumber





def getNewAlarm(startIdAlarm, numberErrorConnect, not_connect):

    TOKEN = config.TOKEN  # Токен бота
    database = config.database  # Конфигурация для подключения к БД
    time_connect = config.time_connect  # Время цикла mопроса БД
    mySQLQuery_1 = config.mySQLQuery_1  # Вариант первого запроса к базе
    mySQLQuery_2 = config.mySQLQuery_2  # Вариант второго запроса к базе(если IDAlarm >2000000)

    listNewAlarmID = []            # Список ID новых авварий
    listDiscriptionNewAlarm = []   # Список с описанием новых аварий
    lastAlarmID = startIdAlarm     # ID предыдущей аварии
    i = numberErrorConnect         # Начальное значение для отсчета ошибок подключения
    result = {}

    db = data_base.SQL(database)  # подключение к БД

    """ Проверка на наличие ошибок подключения > 5 выдаем сообщение"""
    if db.err_connect == True:
        if i < 5:
            i += 1
        else :
            not_connect = True

        result["systemDescription"] = []
        result["lastAlarmID"] = []
    else:
        i = 0
        not_connect = False
        try:
            if lastAlarmID > 2000000:
                sQLQuery = mySQLQuery_2
            sQLQuery = mySQLQuery_1
            lastAlID = [lastAlarmID]  # ID последней аварии
            db_data = db.import_data(sQLQuery, lastAlID)  # достаем данные из базы
            db.close_connect
        except Exception:
            db.close_connect
            result["systemDescription"] = []
            result["lastAlarmID"] = []
            result["errorConnect"] = True
        extr_data = Processing(db_data)
        alarmEntryId = extr_data.extract_data(1)  # создаем список с ID аварий
        systemDescription = extr_data.extract_data(2)  # создаем список с описанием аварий

        if alarmEntryId:
            if lastAlarmID < 2000000:
                lastAlarmID = max(alarmEntryId)
            elif min(alarmEntryId) < 1000:
                lastAlarmID = min(extractListMinNumber(alarmEntryId))

        result["systemDescription"] = systemDescription
        result["lastAlarmID"] = lastAlarmID

    result["errorConnect"] = not_connect
    result["numberErrorConnect"] = i


    return result

if __name__ == '__main__':
    getNewAlarm('78000')



    





