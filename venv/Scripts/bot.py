import telebot
from config import TOKEN, time_connect
from data_processing import getNewAlarm
import queue
from threading import Thread
import asyncio
from datetime import datetime


# TOKEN = '754652676:AAEgGmoZvQLPHgMITvUn89ww8l8wd7VhYyk'
#329051835
def bot():
    bot = telebot.TeleBot(TOKEN)
    chat_id =[519434051]
    @bot.message_handler(commands=['start'])
    async def send_welcome(message):
        bot.reply_to(message, "Здорово лошара, не знаешь что делать - набирай '/help'")
        if (message.chat.id in chat_id) == False:
            chat_id.append(message.chat.id)
        print(chat_id)

    @bot.message_handler(commands=['help'])
    async def send_help(message):
        bot.reply_to(message, "А ничего делать и не надо, все автоматизировано")
        if (message.chat.id in chat_id) == False:
            chat_id.append(message.chat.id)
        print(chat_id)

    # def sendMessage(textMessage):
    #     bot.send_message(chat_id, textMessage )

    async def sendMessage(chat_id,time_connect):
        while True:
            await asyncio.sleep(time_connect)

            result = getNewAlarm()

            await bot.send_message(chat_id, textMessage )

    # qe = queue.Queue()
    th = Thread(target=sendMessage, args = [chat_id, time_connect])
    # result = qe.get()
    # print(result)
    #
    th.start()
    bot.polling()

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
#@bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     for i in chat_id:
#         bot.send_message(i,message.text)
#     bot.reply_to(message, message.text)

if __name__ == '__main__':
    bot()

