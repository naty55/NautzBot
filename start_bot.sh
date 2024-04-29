#!/bin/sh

echo "Fetching latest version from master..." 
git fetch https://github.com/naty55/NautzBot.git > /dev/null 2>&1 

echo "Installing dependencies..."
pip install -r requirements.txt > /dev/null

bot_token=`cat token.txt`

echo "Starting Bot..."
python3 NautzBot.py