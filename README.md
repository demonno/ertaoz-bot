# Ertaoz Bot
![Github actions](https://github.com/demonno/ertaoz-bot/workflows/bothealth/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Install

### Setup python virtual env on Linux

    sudo apt install python3.7 python3-venv python3.7-venv
    python3.7 -m venv venv

### Activate env

    source venv/bin/activate

### Install packages in `venv`

    make install


## Create Test Bot using Botfather

For testing prurposes its recommended to have a separate testing bot.
Read docs about how to create a bot [here](https://core.telegram.org/bots#3-how-do-i-create-a-bot).
After you will get token which you can set in `.env` file


## Run bot

    python main.py


## Run formatters

    make fmt

## Run linters

    make lint

## Contribution Guidelines

* Create New Issue: https://github.com/demonno/ertaoz-bot/issues/new
* Link issue to https://github.com/demonno/ertaoz-bot/projects
* Work on your branch, branch naming policy e{issue_number}
* Create Pull Request and ask for reviews
* Add `fixes #{issue_number}` in the body of pull request
* Delete your branch after merge
* After merging to master bot is deployed automatically

[Read How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)
