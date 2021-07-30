import json
import os

""" Считываем данные из файла config.json"""
with open('config.json', 'r', encoding = 'utf-8') as f:
    configData = json.load(f)
    TOKEN = configData['TOKEN']                  # Токен бота
    database = configData['database']            # Конфигурация для подключения к БД
    time_connect = int(configData['time_connect'])    # Время циклаопроса БД
    mySQLQuery_1 = str(configData['mySQLQuery_1'])   # Вариант первого запроса к базе
    mySQLQuery_2 = configData['mySQLQuery_2']    # Вариант второго запроса к базе(если IDAlarm >2000000)
    startIdAlarm = int(configData['startIdAlarm'])    # Значение IdAlarm при запуске программы
