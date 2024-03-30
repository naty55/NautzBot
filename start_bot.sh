#!/bin/sh

git fetch https://github.com/naty55/NautzBot.git
pip install -r requirements.txt

bot_token=`cat token.txt`

python3 NautzBot.py