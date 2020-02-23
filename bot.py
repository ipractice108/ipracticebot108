import telebot
import constants
import os
import random
import urllib.request as urllib2
import webbrowser
import parser
# from bs4 import BeautifulSoup


bot = telebot.TeleBot(constants.token)
upd = bot.get_updates()
#   print(upd)

last_upd = upd[-1]
message_from_user = last_upd.message
print(message_from_user)

print(bot.get_me())

def log(message, answer):
  print("\n -----")
  from datetime import datetime
  print(datetime.now())
  print("Сообщение от (0) (1), (id = (2)) \n Текст - (3)".format(message.from_user.first_name,
                                                                 message.from_user.last_name,
                                                                 str(message.from_user.id),
                                                                 message.text))
  print(answer)

# @bot.message_handler(commands=['help'])
# def handle_text(message):
#   bot.send_message(message.chat.id, "Это просто пушка дичайшая")

@bot.message_handler(content_types=['text', 'video'])
def handle_text(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, 'Здравствуйте! Вас приветствует чат бот ipractice.club '
                                          'Для вас комплексы упражнений для укрепления всего опорно двигательного аппарата, развития силы, гибкости и равновесия.'
                                          'Выберите свой уровень и занимайтесь'
                                          
                                          '/новичек' 
                                          '3 видео урока для тех, кто давно не занимался и чувствует что пора начинать.'
                                          
                                          '/средний'
                                          '4 видео урока для тех, кто уже занимается 1-2 года и ищет полезных упражнений для развития.'
                                          
                                          '/продвинутый'
                                          '5 видеоуроков для тех, кто регулярно занимается дома 5 лет и возможно думаете о препподавании или уже преподаёте друзьям.')
    elif message.text == "/новичек":
        bot.send_message(message.chat.id, 'посмотрите бесплатный видео урок на канале  -                                                                 https://www.youtube.com/watch?v=2j3MsZ4E6iQ&feature=youtu.be')
        bot.send_message(message.chat.id, "Ну как? Вы разогрелись? Все получается?")
        bot.send_message(message.chat.id, "Поздравляем! Вы получили ознакомительный видео урок и он остается у Вас в доступе. "
                                          "Хотите начать следующее занятие и получить доступ к полному курсу «новичек» на год, за 300₽  - нажмите /курсНовичек")
        key = telebot.types.ReplyKeyboardMarkup(True,False)
        key.row('зарегистрироваться на вебинар', 'полезные книги', 'помощь', 'туры')
        send = bot.send_message(message.chat.id, "Рад видеть Вас заряженными и вдохновленными", reply_markup=key)
    elif message.text == "/средний":
        answer = "Пожалуйста напишите                                                                       Имя                                                                                        Контактный телефон или почту                                                                                                  "
        bot.send_message(message.chat.id, "Пожалуйста напишите                                                                       Имя                                                                                        Контактный телефон или почту                                                                                            ")
        log(message, answer)
    elif message.text == "/ready":
        bot.send_message(message.chat.id, 'пожалуйста внимательно выполняйте упражнения после разогрева                                                                                                           https://youtu.be/NYxhZYpw1HQ')
    elif message.text == "зарегистрироваться на вебинар":
        bot.send_message(message.chat.id, 'пожалуйста заполните форму обратной связи на сайте https://ipractice.club')
    elif message.text == "полезные книги":
        urllib2.urlretrieve('http://youtu.be/bTVNW4wTOXw')

    else:
        bot.send_message(message.chat.id, "Превосходно, теперь напишите /ready")


bot.polling(none_stop=True)




