import schedule
import threading
import os, sys
import telebot,time
import re
import requests
import proc
import pb
import config
import json
import proverka
 
bot = telebot.TeleBot("5621846479:AAFyD6toWPzw4YM-2oSIBLqEWZ9k3ffK5lw")
 
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Welcome to the Haqq bot!\nAdd your validators. The bot will automatically notify if the validator goes to jail\n/help')
 
@bot.message_handler(commands=['help'])
def help_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Написать разработчику', url='telegram.me/tarabukinivan'))
    tmp = 'Команды бота: \n /help - справка по боту'
    tmp = tmp + ' \n/add <valoperaddr> - добавить валидатора'
    tmp = tmp + ' \n/my - список моих валидаторов'
    tmp = tmp + ' \n/info - информация о моих валидаторах'
    tmp = tmp + ' \n/del - удалить все валидаторы'
    bot.send_message(message.chat.id,tmp,reply_markup=keyboard)
 
@bot.message_handler(commands=['add'])
def help_message(message):
    try:
        val = message.text.split(maxsplit=1)[1]
    except IndexError:
        val = ''
 
    if(val):
        tmp = pb.writeval(message.from_user.id,val)
        bot.send_message(message.chat.id, tmp)
 
@bot.message_handler(commands=['my'])
def help_message(message):
    tmp = pb.myval(message.from_user.id)
    bot.send_message(message.chat.id,tmp)
 
@bot.message_handler(commands=['del'])
def help_message(message):
    tmp = pb.delval(message.from_user.id)
    bot.send_message(message.chat.id,'Все ваши валики удалены')
 
@bot.message_handler(commands=['info'])
def help_message(message):
    tmps = pb.infoval(message.from_user.id)
    bot.send_message(message.chat.id,tmps)
 
def sending():
    st = str(proverka.provval())
    tmpr = st.split(",")
    tmpr.pop()
    for key in range(len(tmpr)):
        user_id = tmpr[key].split()[0]
        valik = tmpr[key].split(maxsplit=2)[1]
        bot.send_message(str(user_id), 'валидатор ' + valik + ' в тюрьме')
 
@bot.message_handler(func=lambda message: message.text.lower() in ['привет', 'здравствуйте'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте!")
 
@bot.message_handler(func=lambda message: message.text.lower() in ['ваня','вася'])
def text(message):
    if message.text.lower() == 'ваня':
        bot.send_message(message.chat.id,'Привет Ваня'+ str(message.from_user.id))
    if message.text.lower() == 'вася':
        bot.send_message(message.chat.id,'Сам ты Вася')
 
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, 'Я тебя не понимаю')

def runBot():
    bot.polling(none_stop=True)

def runScheluders():
    schedule.every(10).minutes.do(sending)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    t1 = threading.Thread(target=runBot)
    t2 = threading.Thread(target=runScheluders) 
    t1.start()
    t2.start()

#bot.infinity_polling(timeout=30, long_polling_timeout = 15)

#while True:
 #   try:
  #      sending()
   #     bot.polling(timeout=30, long_polling_timeout = 15)
   # except Exception as e:
    #    print(e)
     #   time.sleep(5)
      #  continue
