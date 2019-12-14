import argparse

from bots.ertaoz import ertaoz_bot
from bots.noshrevan import noshrevan_bot
from bots.qristefore import qristefore_bot


def parse_args():
    parser = argparse.ArgumentParser(description="Cli to run different bots")
    parser.add_argument(
        "-b",
        "--bot",
        dest="bot_username",
        type=str,
        choices=[ertaoz_bot.BOT_USERNAME, qristefore_bot.BOT_USERNAME, noshrevan_bot.BOT_USERNAME],
        default=ertaoz_bot.BOT_USERNAME,
        help=f"Specify which bot to run(default: {ertaoz_bot.BOT_USERNAME})",
    )
    arguments = parser.parse_args()
    return arguments


if __name__ == "__main__":
    arguments = parse_args()
    if arguments.bot_username == ertaoz_bot.BOT_USERNAME:
        ertaoz_bot.run()
    elif arguments.bot_username == qristefore_bot.BOT_USERNAME:
        qristefore_bot.run()
    elif arguments.bot_username == noshrevan_bot.BOT_USERNAME:
        noshrevan_bot.run()
    else:
        raise Exception(f"{arguments.bot_username} not supported")
