# coding: utf-8
from utils import getUserName
from db import AppDb
import telegram

db = AppDb()

def start(bot, update): 
    update.message.reply_text("Hi.")

def addTag(bot, update):
    chatId = update.message.chat_id
    if update.message.reply_to_message:
        replyTo = update.message.reply_to_message.from_user.id
    else:
        replyTo = update.message.from_user.id
    fromUser = update.message.from_user.id
    if db.isLimied(fromUser):
        update.message.reply_text(u"操作被拒绝: 速率限制", 
            reply_to_message_id=update.message.message_id)
    db.addLimit(fromUser, chatId)

    for item in str(update.message.text).split(" "):
        tag = update.message.text[5:]
        db.addTag(replyTo, chatId, tag)

    if update.message.from_user:
        db.setUserName(getUserName(update.message.from_user), fromUser)

    if update.message.reply_to_message:
        db.setUserName(getUserName(update.message.reply_to_message.from_user), replyTo)

    update.message.reply_text(u"操作成功 添加了Tag", 
            reply_to_message_id=update.message.message_id)

def listTag(bot, update, args):
    chatId = update.message.chat_id
    if len(args) == 0:
        update.message.reply_text(ur"请使用 /listtag { Tag名称 } 来使用", 
            reply_to_message_id=update.message.message_id)
        return
    tag = "".join(args)
    replyText = u"显示 **{}** 的结果: \n\n".format(tag)
    index = 1
    for item in db.listTag(chatId, tag):
        if not item['tags'].has_key(tag):
            continue
        userId = item['userId']
        userName = db.getUserName(userId)
        replyText += str(index) + '. ' + userName + " - " + str(item['tags'][tag]) + '\n'

        index += 1
    update.message.reply_text(replyText, 
        reply_to_message_id=update.message.message_id, 
        parse_mode=telegram.ParseMode.MARKDOWN)

def help(bot, update):
    pass