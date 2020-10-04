import click

from src import settings
from src.ertaoz import ertaoz_bot

BOT_NAMES = [ertaoz_bot.BOT_USERNAME]


@click.command()
def cli():
    ertaoz_bot.run(token=settings.BOT_ERTAOZ_TOKEN)


if __name__ == "__main__":
    cli()
