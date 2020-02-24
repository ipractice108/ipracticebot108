import os
import constants

from bot import bot
from telebot import types
from flask import Flask, request
 
server = Flask(__name__)
 
@server.route('/' + constants.token, methods=['POST'])
def get_message():
    bot.process_new_updates([types.Update.de_json(
         request.stream.read().decode("utf-8"))])
    return "!", 200
 
@server.route('/', methods=['GET'])
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=constants.heroku_url + constants.token)
    return "Hello from Heroku!", 200
 
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))