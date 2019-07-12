# coding: utf-8
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


updater = Updater('842234941:AAEVoSwgpolP7dHwRJmuH1OsAVhdF7TD3Qo')
dispatcher = updater.dispatcher

def start(bot, update):        
    bot.send_message(chat_id=update.message.chat_id, text="ქრისტეფორე მგალობლიშვილი გარიყულადან.")

dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
