#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from telegram import ParseMode
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from telegram.ext.dispatcher import run_async
import random

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN = "726693597:AAGuNw5J2QiDc-C7DKr2Sa4gaQFJy51E4Bc"
BOTNAME = "ertaoz_bot"


help_text = """ერთაოზი ძუყნურიდან!
\nბრძანებები:\n
/`cat` - კატის ფოტოს გამოგზავნა
/`order` - ჩატში წესრიგის დამყარება
/`when_who` - ვიზეარის ფრენების სია

/`ბრძანება@ertaoz_bot p1 p2`


მაგალითად:

/cat@ertaoz\_bot
/cat@ertaoz\_bot cute
/cat@ertaoz\_bot funny
/cat@ertaoz\_bot says Love
/cat@ertaoz\_bot cute says Love

"""

wisdoms = [
    ("სიყვარული ვერტიკალურია და თან ბრუნვადი",
     "https://s4.gifyu.com/images/love.gif"),
    ("არა, ყმაწვილო, არა! ასეთი ცოდნით ვერ გავფრინდებით, არადა, უნდა გავფრინდეთ!",
     "https://thumbs.gfycat.com/AdventurousColossalBobwhite-size_restricted.gif"),
    ("რომელია ჩვენს შორის მართალი, იქ გამოჩნდება, ზეცაში!",
     "https://thumbs.gfycat.com/RelievedSardonicGoa-size_restricted.gif"),
    ("სიყვარული... სიყვარულია მშობელი ოცნებისა, ოცნება აღვიძებს კაცთა მოდგმის მთვლემარე გონებას, გონება აღძრავს ქმედებას, პლიუს-მინუს, ემ ცე კვადრატ (mc²), ეф, ფუძე (√) ვნებათაღელვის უსასრულობისა და შეცნობილი აუცილებლობისაკენ! მიდით ერთაოზ!",
     "https://i.makeagif.com/media/7-09-2015/gLIbf3.gif")
]


@run_async
def send_async(update, context, *args, **kwargs):
    context.bot.sendMessage(chat_id=update.effective_chat.id, **kwargs)


@run_async
def send_async_gif(update, context, *args, **kwargs):
    context.bot.sendAnimation(
        chat_id=update.effective_chat.id, *args, **kwargs)

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.


def start(update, context):
    update.message.reply_text("ერთაოზ ბრეგვაძე ძუყნურიდან!")


def cat(update, context):
    cat_photo_url = "https://cataas.com/cat/"
    if context.args:
        cat_photo_params = "/".join(context.args)
        cat_photo_url = cat_photo_url + cat_photo_params
    if cat_photo_url.endswith("/"):
        cat_photo_url = cat_photo_url[:-1]
    context.bot.sendPhoto(
        chat_id=update.effective_chat.id, photo=cat_photo_url)


def order(update, context):
    send_async_gif(update, context, caption="დახურეთ საინფორმაციო წყარო!",
                   animation="https://s4.gifyu.com/images/shush.gif",)


def when_who(update, context):
    txt = """
`11-05` = 
`15-09` = 
`15-05` = 
`18-04` = 
`18-04` = 
`22-05` = 
`22-05` = 
`22-05` = 
`22-05` = 
`22-12` = 
`22-12` = 
`22-12` = 
`22-19` = 
"""
    # update.message.reply_text(txt)
    if update.effective_chat.id != -360632460:
        send_async(update, context, text="აქ ვერ გეტყვი.")
    else:
        send_async(update, context, text=txt,
                   parse_mode=ParseMode.MARKDOWN)


def wisdom(update, context):
    randomWisdom = random.choice(wisdoms)
    send_async_gif(update, context, caption=randomWisdom[0],
                   animation=randomWisdom[1])

# Introduce the bot to a chat its been added to


def introduce(update, context):
    """
    Introduces the bot to a chat its been added to and saves the user id of the
    user who invited us.
    """

    chat_id = update.effective_chat.id
    invited = update.message.from_user.id

    logger.info(
        "Invited by {} to chat {} ({})".format(
            invited, chat_id, update.message.chat.title
        )
    )

    text = "გამარჯობა {}! მე ვარ ერთაოზ ბრეგვაძე ძუკნურიდან. მე გავუიასნებ ხოლმე ამ ჩატის მიზანს ყველას ვინც შემოგვიერთდება :)".format(
        update.message.chat.title
    )
    send_async(update, context, text=text)


def welcome(update, context, new_chat_member):
    """ Welcomes a user to the chat """

    message = update.message
    chat_id = message.chat.id
    logger.info(
        "{} joined to chat {} ({})".format(
            new_chat_member["first_name"], chat_id, message.chat.title
        )
    )

    text = """გამარჯობა {username}! კეთილი იყოს შენი მობრძანება {title}-ში :)

    {username} დაწერე რა დღეებში ხარ საქართველოში.

    გისურვებ ბედნიერ ახალი წლის დღეებს :) <3
    """

    # Replace placeholders and send message
    text = text.format(
        username=new_chat_member["first_name"], title=message.chat.title)
    send_async(update, context, text=text)


def goodbye(update, context):
    """ Sends goodbye message when a user left the chat """

    message = update.message
    chat_id = update.effective_chat.id
    logger.info(
        "{} left chat {} ({})".format(
            message.left_chat_member.first_name, chat_id, message.chat.title
        )
    )

    text = "ნახვამდის, $username! :( "

    # Replace placeholders and send message
    text = text.replace("$username", message.left_chat_member.first_name).replace(
        "$title", message.chat.title
    )
    send_async(update, context, text=text, parse_mode=ParseMode.HTML)


def empty_message(update, context):
    """
    Empty messages could be status messages, so we check them if there is a new
    group member, someone left the chat or if the bot has been added somewhere.
    """

    if (
        hasattr(update.message, "new_chat_members")
        and len(update.message.new_chat_members) > 0
    ):
        new_members = update.message.new_chat_members
        for new_chat_member in new_members:
            # Bot was added to a group chat
            if new_chat_member["username"] == BOTNAME:
                return introduce(update, context)
            # Another user joined the chat
            else:
                return welcome(update, context, new_chat_member)

    # Someone left the chat
    elif hasattr(update.message, "left_chat_member"):
        if update.message.left_chat_member.username != BOTNAME:
            return goodbye(update, context)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def help(update, context):
    send_async(update, context, text=help_text,
               parse_mode=ParseMode.MARKDOWN)


def main():
    """Run bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("cat", cat))
    dp.add_handler(CommandHandler("order", order))
    dp.add_handler(CommandHandler("when_who", when_who))
    dp.add_handler(CommandHandler("wisdom", wisdom))

    dp.add_handler(MessageHandler(Filters.status_update, empty_message))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
