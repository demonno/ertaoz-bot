# coding: utf-8
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


updater = Updater('684288261:AAHtV3VYrhrcRKOKPzv0HZrCt4hfB41dBxU')
dispatcher = updater.dispatcher


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="მე ვარ ნოშრევანი, ვაკეტებ ბროწეულის ოყნებს!")

def echo(bot, update):
    print("Incoming: {}".format(update.message.text))
    bot.send_message(chat_id=update.message.chat_id, text="აბე გლოკოზააა!")
    
echo_handler = MessageHandler(Filters.text, echo)

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()
