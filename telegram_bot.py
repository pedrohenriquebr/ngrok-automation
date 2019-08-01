# Telegram modules
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging

# Settings modules
import os
import sys
import settings

# Ngrok service modules
from ngrok_service import NgrokService

email = os.getenv("SMTPCLIENT_EMAIL")
password = os.getenv("SMTPCLIENT_PASSWORD")
service = NgrokService(email,password)

if email is None or password is None:
	print("You have to declare SMTPCLIENT_EMAIL and SMTPCLIENT_PASSWORD!")
	exit(1)

updater = Updater(token=os.getenv('AUTH_TOKEN'),use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# /start
def start(update, context):

    if update.message.from_user.username != os.getenv("TELEGRAM_USERNAME"):
        context.bot.send_message(chat_id=update.message.chat_id,text="You're blocked!")
        return
    
    context.bot.send_message(chat_id=update.message.chat_id, text="Send ngrok command:\n\n<protocol> <port>")

# /stop
def stop(update, context):

    if update.message.from_user.username != os.getenv("TELEGRAM_USERNAME"):
        context.bot.send_message(chat_id=update.message.chat_id,text="You're blocked!")
        return
    
    context.bot.send_message(chat_id=update.message.chat_id, text="Stopping...")
    service.stop()

def echo(update, context):
    
    if update.message.from_user.username != os.getenv("TELEGRAM_USERNAME"):
        context.bot.send_message(chat_id=update.message.chat_id,text="You're blocked!")
        return
    
    context.bot.send_message(chat_id=update.message.chat_id, text="Starting {}...".format(update.message.text.lower()))
    msg  = service.start(update.message.text.lower())
    context.bot.send_message(chat_id=update.message.chat_id,text=msg)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

stop_handler = CommandHandler('stop', stop)
dispatcher.add_handler(stop_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()


