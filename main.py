from telegram.ext import Updater, CommandHandler
from config import BOT_ID
from db import AppDb
import logging
import json

db = AppDb()
logging.getLogger().setLevel(logging.DEBUG)

def start(bot, update): 
    update.message.reply_text("Hi.")

# Impl rich for first
# TODO: wildcard match tag
def rich(bot, update):
    if update.message.reply_to_message:
        charId = update.message.chat_id
        chatId = update.message.chat_id
        replyTo = update.message.reply_to_message.from_user.id
        update.message.reply_text('You reply to message' + str(replyTo))
        db.addTag(replyTo, chatId, 'rich')
        update.message.reply_text('Added rich to ' + str(replyTo))
    else:
        update.message.reply_text("???")
    

def listRich(bot, update):
    chatId = update.message.chat_id
    update.message.reply_text(json.dumps(db.listTag(chatId, 'rich')))

def main():
    bot = Updater(token=BOT_ID)

    dp = bot.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('rich', rich))
    dp.add_handler(CommandHandler('listrich', listRich))


    bot.start_polling()
    bot.idle()

if __name__ == "__main__":
    main()