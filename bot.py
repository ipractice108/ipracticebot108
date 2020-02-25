# -*- coding: utf-8 -*-
import os
import urllib
import logging
import telebot
import constants

bot = telebot.TeleBot(constants.token)

upd = bot.get_updates()
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

# upd = bot.get_updates()
# last_upd = upd[-1]
# message_from_user = last_upd.message
# print(message_from_user)

print(bot.get_me())

def log(message, answer):
  print("\n -----")
  from datetime import datetime
  print(datetime.now())
  print("Сообщение от {} {}, (id = {}) \n Текст - {}".format(message.from_user.first_name,
                                                                 message.from_user.last_name,
                                                                 str(message.from_user.id),
                                                                 message.text))
  print(answer)

# @bot.message_handler(commands=['help'])
# def handle_text(message):
#   bot.send_message(message.chat.id, "Это просто пушка дичайшая")

@bot.message_handler(content_types=['text', 'video'])
def handle_text(message):
    print("message text is: " + message.text)
    if message.text == "/start":
        key.row('зарегистрироваться на вебинар', 'полезные книги')
        key.row('марафон', 'туры')
        send = bot.send_message(message.chat.id, 'Здравствуйте! Вас приветствует чат бот ipractice.club', reply_markup=key)
        bot.send_message(message.chat.id, 'Для вас комплексы упражнений для укрепления всего опорно двигательного аппарата, развития силы, гибкости и равновесия.\n'
                                          '\n'
                                            'Выберите свой уровень и занимайтесь\n'
                                           '\n')
        bot.send_message(message.chat.id, '/beginner - начинающий\n'
                                          '3 видео урока для тех, кто давно не занимался и чувствует что пора начинать.\n'
                                            '\n')
        bot.send_message(message.chat.id, '/middle  - средний\n'
                                          '4 видео урока для тех, кто уже занимается 1-2 года и ищет полезных упражнений для развития.\n'
                                            '\n')
        bot.send_message(message.chat.id, '/pro - продвинутый\n'
                                          '5 видеоуроков для тех, кто регулярно занимается дома 5 лет и возможно думаете о преподавании или уже преподаёте друзьям.\n')

    elif message.text == "/beginner":
        bot.send_message(message.chat.id, 'http://youtu.be/8EgiMc5iwGg')
        bot.send_message(message.chat.id,
                         'Поздравляем! Вы получили ознакомительный видео урок и он остается у Вас в доступе!\n'
                         '\n'
                         'Хотите начать следующее занятие и получить доступ к полному курсу «новичек» на год, за 3000₽                                                        - нажмите -> /GoBeginner\n'
                         '\n'
                         'Хотите участвовать в перосональном, недельном онлайн марафоне "Я ВСЕ МОГУ" за 1000₽                                                                - нажмите -> /marathon\n'
                         '\n'
                         'Хотите индивидуальную консультацию или занятие - нажмите -> /individual\n'
                         '\n'
                         'Хотите записаться на физическое групповое занятие в Москве                                                                                         - нажмите -> /group\n')

    elif message.text == "/middle":
        bot.send_message(message.chat.id, 'https://youtu.be/2j3MsZ4E6iQ')
        bot.send_message(message.chat.id, 'Поздравляем! Вы получили ознакомительный видео урок и он остается у Вас в доступе!\n'
                                        '\n'
                                        'Хотите начать следующее занятие и получить доступ к полному курсу «средний» на год, за 3000₽                                                        - нажмите -> /GoMiddle\n'
                                        '\n'
                                        'Хотите участвовать в перосональном, недельном онлайн марафоне "Я ВСЕ МОГУ" за 1000₽                                                                - нажмите -> /marathon\n'
                                        '\n'
                                        'Хотите индивидуальную консультацию или занятие - нажмите -> /individual\n'
                                        '\n'
                                        'Хотите записаться на физическое групповое занятие в Москве                                                                                         - нажмите -> /group\n')
if __name__ == '__main__':
    bot.polling(none_stop=True)
