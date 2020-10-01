# Ertaoz Bot
![Github actions](https://github.com/demonno/telegram_bots/workflows/bothealth/badge.svg)

![Logo](art/logo.png)

## Install

### Setup python virtual env on Linux

    sudo apt install python3.7 python3-venv python3.7-venv
    python3.7 -m venv venv

### Activate env

    source venv/bin/activate

### Install packages in `venv`

    pip install -r requirements.txt


## Create Test Bot using Botfather 

For testing prurposes its recommended to have a separate testing bot.
Read docs about how to create a bot [here](https://core.telegram.org/bots#3-how-do-i-create-a-bot).
After you will get token which you can set in `.env` file

## Enviroment Variables

Tokens secrets and configurations stored in `.env` file, create locally. !do not commit in git!

```ini
ERTAOZ_TOKEN=

WEATHER_API_ID=
IMGFLIP_API_USERNAME=
IMGFLIP_API_PASSWORD=

ERROR_REPORTING=false
ERROR_REPORTING_CHAT_ID=-00000000

```

## Run locally

To run default bot:

    python main.py

Or explicitly

    python main.py --bot ertaoz_bot

Check out `--help` to run other bots

    python main.py -h
    python main.py --bot noshrevan_bot
    python main.py --bot qristefore_bot


## Run black formatter

    black .

### Vscode -

Install extension: `ms-python.python`

To Setup with VS Code: https://github.com/psf/black#visual-studio-code


## Contribution Guidelines

* Create New Issue: https://github.com/demonno/telegram_bots/issues/new
* Link issue to https://github.com/demonno/telegram_bots/projects
* Work on your branch, branch naming policy e{issue_number}
* Create Pull Request and ask for reviews
* Add `fixes #{issue_number}` in the body of pull request
* Delete your branch after merge
* After merging to master bot is deployed automatically

[Read How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
