import aiogram
from config import TOKEN, time_connect, startIdAlarm
from data_processing import getNewAlarm
import queue
from threading import Thread
import asyncio
from datetime import datetime

#610528633
#329051835
bot = aiogram.Bot(TOKEN)
dp = aiogram.Dispatcher(bot)
chat_id = [519434051]
lastAlarmID = startIdAlarm
numberErrorConnect = 0
errorConnect = False


@dp.message_handler(commands=['start'])
async def send_welcome(message: aiogram.types.Message):
    if (message.chat.id in chat_id) == False:
        chat_id.append(message.chat.id)
        print(chat_id)
    await   message.answer("Ваш ID добавлен в список рассылки")

@dp.message_handler(commands=['help'])
async def send_help(message: aiogram.types.Message):
    if (message.chat.id in chat_id) == False:
        chat_id.append(message.chat.id)
    await   message.answer("Привет, никаких команд пока нет, ID добавляется в\
                            список при наборе любой из команд '/start' или '/help',\
                            после перезапуска программы список удаляется")

async def sendMessage(chat_id, time_connect, lastAlarmID, numberErrorConnect, errorConnect):
    while True:
        await asyncio.sleep(time_connect)

        result = getNewAlarm(lastAlarmID, numberErrorConnect, errorConnect)
        sistemDescriptionAlarm =  result["systemDescription"]
        lastAlarmID = result["lastAlarmID"]
        numberErrorConnect = result["numberErrorConnect"]

        if sistemDescriptionAlarm:
            for i in chat_id:
                await bot.send_message(i, sistemDescriptionAlarm)

        if (errorConnect == False and result["errorConnect"] == True):
            errorConnect = True
            for i in chat_id:
                await bot.send_message(i, "Ошибка соединения с БД")
        elif (errorConnect == True and result["errorConnect"] == False):
            errorConnect = False


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(sendMessage(chat_id, time_connect, lastAlarmID, numberErrorConnect, errorConnect))
    aiogram.executor.start_polling(dp, skip_updates = True)









