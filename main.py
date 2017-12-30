# coding: utf-8
from telegram.ext import Updater, CommandHandler, RegexHandler
from config import BOT_ID
from func import *
import logging

logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)


def main():
    bot = Updater(token=BOT_ID)

    dp = bot.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(RegexHandler('^/tag@(a-zA-Z0-9)*', addTag))
    dp.add_handler(CommandHandler('listtag', listTag, pass_args=True))

    bot.start_polling()
    bot.idle()

if __name__ == "__main__":
    main()