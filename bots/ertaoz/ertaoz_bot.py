#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from datetime import datetime

import pytz
from telegram import ParseMode
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from telegram.ext.dispatcher import run_async
import random

# Enable logging
from bots import env
from bots.apis.weather_api import Weather
from bots.ertaoz.models import Wisdom
from bots.utils.typing import send_typing_action

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = "726693597:AAGuNw5J2QiDc-C7DKr2Sa4gaQFJy51E4Bc"
BOT_USERNAME = "ertaoz_bot"


help_text = """ერთაოზი ძუყნურიდან!
\nბრძანებები:\n
/`cat` - კატის ფოტოს გამოგზავნა
/`order` - ჩატში წესრიგის დამყარება
/`when_who` - ვიზეარის ფრენების სია
/`weather` - ამინდის პროგნოზი
/`about` - ინფორმაცია შემქმნელებზე
/`who_is_ertaoz` - ინფორმაცია ერთაოზზე

/`ბრძანება@ertaoz_bot p1 p2`


მაგალითად:

/cat@ertaoz\_bot
/cat@ertaoz\_bot cute
/cat@ertaoz\_bot funny
/cat@ertaoz\_bot says Love
/cat@ertaoz\_bot cute says Love

"""
TEST_GROUP_ID = -353748767
NONAME_GROUP_ID = -360632460

WISDOMS = [
    Wisdom("სიყვარული ვერტიკალურია და თან ბრუნვადი", "https://s4.gifyu.com/images/love.gif"),
    Wisdom(
        "არა, ყმაწვილო, არა! ასეთი ცოდნით ვერ გავფრინდებით, არადა, უნდა გავფრინდეთ!",
        "https://thumbs.gfycat.com/AdventurousColossalBobwhite-size_restricted.gif",
    ),
    Wisdom(
        "რომელია ჩვენს შორის მართალი, იქ გამოჩნდება, ზეცაში!",
        "https://thumbs.gfycat.com/RelievedSardonicGoa-size_restricted.gif",
    ),
    Wisdom(
        "სიყვარული... სიყვარულია მშობელი ოცნებისა, ოცნება აღვიძებს კაცთა მოდგმის მთვლემარე გონებას, გონება აღძრავს ქმედებას, პლიუს-მინუს, ემ ცე კვადრატ (mc²), ეф, ფუძე (√) ვნებათაღელვის უსასრულობისა და შეცნობილი აუცილებლობისაკენ! მიდით ერთაოზ!",
        "https://i.makeagif.com/media/7-09-2015/gLIbf3.gif",
    ),
]

WHEN_WHO = [
    (datetime(day=11, month=12, year=2019), datetime(day=5, month=1, year=2020), ""),
    (datetime(day=15, month=12, year=2019), datetime(day=9, month=1, year=2020), ""),
    (datetime(day=15, month=12, year=2019), datetime(day=5, month=1, year=2020), ""),
    (datetime(day=18, month=12, year=2019), datetime(day=4, month=1, year=2020), ""),
    (datetime(day=18, month=12, year=2019), datetime(day=4, month=1, year=2020), ""),
    (datetime(day=22, month=12, year=2019), datetime(day=5, month=1, year=2020), ""),
    (datetime(day=22, month=12, year=2019), datetime(day=5, month=1, year=2020), ""),
    (datetime(day=22, month=12, year=2019), datetime(day=5, month=1, year=2020), ""),
    (datetime(day=22, month=12, year=2019), datetime(day=5, month=1, year=2020), ""),
    (datetime(day=22, month=12, year=2019), datetime(day=12, month=1, year=2020), ""),
    (datetime(day=22, month=12, year=2019), datetime(day=12, month=1, year=2020), ""),
    (datetime(day=22, month=12, year=2019), datetime(day=12, month=1, year=2020), ""),
    (datetime(day=22, month=12, year=2019), datetime(day=19, month=1, year=2020), ""),
]


@run_async
def send_async(update, context, *args, **kwargs):
    context.bot.sendMessage(chat_id=update.effective_chat.id, **kwargs)


@run_async
def send_async_gif(update, context, *args, **kwargs):
    context.bot.sendAnimation(chat_id=update.effective_chat.id, *args, **kwargs)


@send_typing_action
def start(update, context):
    update.message.reply_text("ერთაოზ ბრეგვაძე ძუყნურიდან!")


@send_typing_action
def cat(update, context):
    cat_photo_url = "https://cataas.com/cat/"
    if context.args:
        cat_photo_params = "/".join(context.args)
        cat_photo_url = cat_photo_url + cat_photo_params
    if cat_photo_url.endswith("/"):
        cat_photo_url = cat_photo_url[:-1]
    context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=cat_photo_url)


@send_typing_action
def order(update, context):
    send_async_gif(
        update, context, caption="დახურეთ საინფორმაციო წყარო!", animation="https://s4.gifyu.com/images/shush.gif",
    )


@send_typing_action
def who_is_ertaoz(update, context):
    text = """Info about Ertaoz... Bregvadze... Son of Mizana Bregvadze:
    Hobbies: physics, building ცათმფრენი, ტიტანური იდეები
    Love interest: მარგალიტა
    Friends: შავი დედალი, ბიძია-ბაბუა (ქრისტეფორე მგალობლიშვილი გარიყულადან)
    ნაციხარი: yes
    Net worth: შავი დედალი
    """
    send_async(update, context, text=text)


@send_typing_action
def when_who(update, context):
    now = datetime.now()
    lines = []
    for outbound, inbound, name in WHEN_WHO:
        if outbound <= now:
            start = "<i>{}</i>".format(str(outbound.day).zfill(2))
        else:
            start = "<b>{}</b>".format(str(outbound.day).zfill(2))

        if inbound <= now:
            end = "<i>{}</i>".format(str(inbound.day).zfill(2))
        else:
            end = "<b>{}</b>".format(str(inbound.day).zfill(2))

        lines.append("{}-{} = <code>{}</code>".format(start, end, name))

    today_txt = "<b>დღეს:</b> {}-{}-{}\n\n".format(datetime.now().day, datetime.now().month, datetime.now().year)
    txt = today_txt + "\n".join(lines)

    if update.effective_chat.id not in [TEST_GROUP_ID, NONAME_GROUP_ID]:
        send_async(update, context, text="აქ ვერ გეტყვი.")
    else:
        send_async(update, context, text=txt, parse_mode=ParseMode.HTML)


@send_typing_action
def wisdom(update, context):
    random_wisdom: Wisdom = random.choice(WISDOMS)
    send_async_gif(update, context, caption=random_wisdom.text, animation=random_wisdom.animation)


@send_typing_action
def about(update, context):
    txt = 'მადლობა ჩემს შემქმნელებს: <a href="https://github.com/demonno">demonno</a>-ს, <a href="https://github.com/pepela">pepela</a>-ს, <a href="https://github.com/dmuml10">dmuml10</a>-სა და <a href="https://github.com/Dgebu">Dgebu</a>-ს'
    send_async(update, context, text=txt, parse_mode=ParseMode.HTML)


# Introduce the bot to a chat its been added to
def introduce(update, context):
    """
    Introduces the bot to a chat its been added to and saves the user id of the
    user who invited us.
    """

    chat_id = update.effective_chat.id
    invited = update.message.from_user.id

    logger.info("Invited by {} to chat {} ({})".format(invited, chat_id, update.message.chat.title))

    text = "გამარჯობა {}! მე ვარ ერთაოზ ბრეგვაძე ძუყნურიდან. მე გავუიასნებ ხოლმე ამ ჩატის მიზანს ყველას ვინც შემოგვიერთდება :)".format(
        update.message.chat.title
    )
    send_async(update, context, text=text)


@send_typing_action
def welcome(update, context, new_chat_member):
    """ Welcomes a user to the chat """

    message = update.message
    chat_id = message.chat.id
    logger.info("{} joined to chat {} ({})".format(new_chat_member["first_name"], chat_id, message.chat.title))

    text = """გამარჯობა {username}! კეთილი იყოს შენი მობრძანება {title}-ში :)

    {username} დაწერე რა დღეებში ხარ საქართველოში.

    გისურვებ ბედნიერ ახალი წლის დღეებს :) <3
    """

    # Replace placeholders and send message
    text = text.format(username=new_chat_member["first_name"], title=message.chat.title)
    send_async(update, context, text=text)


def goodbye(update, context):
    """ Sends goodbye message when a user left the chat """

    message = update.message
    chat_id = update.effective_chat.id
    logger.info("{} left chat {} ({})".format(message.left_chat_member.first_name, chat_id, message.chat.title))

    text = "ნახვამდის, $username! :( "

    # Replace placeholders and send message
    text = text.replace("$username", message.left_chat_member.first_name).replace("$title", message.chat.title)
    send_async(update, context, text=text, parse_mode=ParseMode.HTML)


def empty_message(update, context):
    """
    Empty messages could be status messages, so we check them if there is a new
    group member, someone left the chat or if the bot has been added somewhere.
    """

    if hasattr(update.message, "new_chat_members") and len(update.message.new_chat_members) > 0:
        new_members = update.message.new_chat_members
        for new_chat_member in new_members:
            # Bot was added to a group chat
            if new_chat_member["username"] == BOT_USERNAME:
                return introduce(update, context)
            # Another user joined the chat
            else:
                return welcome(update, context, new_chat_member)

    # Someone left the chat
    elif hasattr(update.message, "left_chat_member"):
        if update.message.left_chat_member.username != BOT_USERNAME:
            return goodbye(update, context)


def error(update, context):
    """Log Errors caused by Updates."""
    message = f"Update {update} \n\n error: \n\n {context.error}"
    logger.warning(message)
    if env.bool("ERROR_REPORTING", False):
        context.bot.send_message(chat_id=env.int("ERROR_REPORTING_CHAT_ID", TEST_GROUP_ID), text=message)


@send_typing_action
def help(update, context):
    send_async(update, context, text=help_text, parse_mode=ParseMode.MARKDOWN)


def notify_about_travelers_job(context):
    today = datetime.now(tz=pytz.timezone("Europe/Tallinn"))

    if today.hour != 9:
        return

    travelers_today = []
    travelers_tomorrow = []

    for outbound, inbound, name in WHEN_WHO:
        difference = outbound.day - today.day
        if 0 <= difference <= 3:
            if outbound.day - today.day == 0:
                travelers_today.append(name)
            elif outbound.day - today.day == 1:
                travelers_tomorrow.append(name)

    message = ""

    if len(travelers_today) == 1:
        travelers_txt = "\n ".join(list(map(lambda x: f"<code>{x}</code>", travelers_today)))
        message = f"ხომ გითხარი, გაფრინდებიან მეთქი, შე გალსტუკიანო! \n მიფრინავს \n {travelers_txt}"
    if len(travelers_today) > 1:
        travelers_txt = "\n ".join(list(map(lambda x: f"<code>{x}</code>", travelers_today)))
        message = f"ხომ გითხარი, გაფრინდებიან მეთქი, შე გალსტუკიანო! \n მიფრინავენ \n {travelers_txt}"
    elif len(travelers_today) == 0:
        if len(travelers_tomorrow) == 1:
            message = "ხვალ მიემგზავრება: " + str(travelers_tomorrow[0])
        elif len(travelers_tomorrow) > 1:
            message = "ხვალ მიემგზავრებიან: " + ", ".join(travelers_tomorrow[:-1]) + " და " + travelers_tomorrow[-1]

    if message != "":
        context.bot.send_message(chat_id=TEST_GROUP_ID, text=message, parse_mode=ParseMode.HTML)
        context.bot.send_message(chat_id=NONAME_GROUP_ID, text=message, parse_mode=ParseMode.HTML)


def weather(update, context):
    api = Weather()
    if context.args:
        weather_info = api.weather_forecast(context.args[0])
    else:
        weather_info = api.weather_forecast("Tallinn")

    send_async(update, context, text=weather_info)


def run(token: str):
    """Run bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(token, use_context=True)
    job = updater.job_queue

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("cat", cat))
    dp.add_handler(CommandHandler("order", order))
    dp.add_handler(CommandHandler("when_who", when_who))
    dp.add_handler(CommandHandler("wisdom", wisdom))
    dp.add_handler(CommandHandler("about", about))
    dp.add_handler(CommandHandler("weather", weather))
    dp.add_handler(CommandHandler("ertaoz", who_is_ertaoz))

    dp.add_handler(MessageHandler(Filters.status_update, empty_message))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # schedule a job every hour min(60 * 60)
    job.run_repeating(notify_about_travelers_job, interval=3600, first=0)

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()
