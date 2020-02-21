import os
import flask
import constants
from bot import bot
from telebot import types
 
server = flask.Flask(__name__)
 
@server.route('/' + constants.token, methods=['POST'])
def get_message():
    bot.process_new_updates([types.Update.de_json(
         flask.request.stream.read().decode("utf-8"))])
    return "!", 200
 
@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=constants.heroku_url + constants.token)
    print("Webhook registered")
    return "Hello from Heroku!", 200
 
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))