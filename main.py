import click
from environs import Env

from bots.ertaoz import ertaoz_bot

BOT_NAMES = [ertaoz_bot.BOT_USERNAME]


@click.command()
@click.option("--bot", type=click.Choice(BOT_NAMES), default=ertaoz_bot.BOT_USERNAME)
def cli(bot):
    env = Env()
    env.read_env()

    if bot == ertaoz_bot.BOT_USERNAME:
        ertaoz_bot.run(token=env.str("ERTAOZ_TOKEN"))


if __name__ == "__main__":
    cli()
