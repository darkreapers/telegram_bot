#import re
#from flask import Flask, request
#import telegram
#from telegram.passport.credentials import bot_token, bot_user_name,URL

#imports
import os
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
#from wit import Wit

"""bot credentials"""
TOKEN = '5522846609:AAG4AM_8c_S7RHpruQJKbOugjUmRImb2qbU'
PORT = int(os.environ.get('PORT', 8433))
BOT_USER_NAME = 'Buddy1234_bot'
URL = "https://buddy-1234.herokuapp.com/"

"""ai token"""
AI_TOKEN = "access token from wit ai"
   
#Enable Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

#Define few commands handlers
def start(update, context):
   """When /start is hit"""
   update.message.reply_text('Hi!')

def help_command(update, context):
   """When /help is hit"""
   update.message.reply_text('Help!')

def google_url(update, context):
    """When /google is hit"""
    update.message.reply_text('https://www.google.co.in/')

def echo(update, context):
   """Echo the user message."""
   update.message.reply_text('Welcome')
   #setting wit ai
#    ai = Wit(access_token = AI_TOKEN)
#    resp = ai.message(update.message.text)

#    print(str(resp))
#    update.message.reply_text(str(resp))

def main():
    """starting bot"""
    updater = Updater(TOKEN, use_context=True)
 
    #getting the dispatchers to register handlers
    dp = updater.dispatcher
    
    #registering commands
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",help_command))
    dp.add_handler(CommandHandler("google",google_url))
    #registering Message Handler to reply to user
    #starting the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
   main()