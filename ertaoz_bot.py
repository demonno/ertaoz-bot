# coding: utf-8
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


updater = Updater('726693597:AAGuNw5J2QiDc-C7DKr2Sa4gaQFJy51E4Bc')
dispatcher = updater.dispatcher

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="ერთაოზ ბრეგვაძე ძუკნურიდან!")

dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
