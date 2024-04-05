#!/usr/bin/env python

import logging
import os
import re
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)
keywords =("קישור", 
           "לינק",
           "קבוצה של",
          "קבוצה ל")
regex = '|'.join(keywords)

async def nautz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if re.search(regex, update.message.text):
        await update.message.reply_text("בנעוץ")


def get_token() -> str:
    token = os.environ.get("bot_token")
    if not token or len(token) <= 0:
        logger.critical("bot_token is not set")
        exit()
    return token


def main() -> None:
    token = get_token()
    application = Application.builder().token(token).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, nautz))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
