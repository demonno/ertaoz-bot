import argparse

from environs import Env

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

    env = Env()
    env.read_env()

    arguments = parse_args()
    if arguments.bot_username == ertaoz_bot.BOT_USERNAME:
        ertaoz_bot.run(token=env.str("ERTAOZ_TOKEN"))
    elif arguments.bot_username == qristefore_bot.BOT_USERNAME:
        qristefore_bot.run(token=env.str("QRISTEFORE_TOKEN"))
    elif arguments.bot_username == noshrevan_bot.BOT_USERNAME:
        noshrevan_bot.run(token=env.str("NOSHREVAN_TOKEN"))
    else:
        raise Exception(f"{arguments.bot_username} not supported")
