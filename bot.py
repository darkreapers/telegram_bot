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
   update.message.reply_text('Hello,I am buddy')

def help_command(update, context):
   """When /help is hit"""
   update.message.reply_text('use /start to start the buddy \n use /list to get list of subject of which notes are available \n To get link of any notes write /(respective no. of subject)')

def subject_list(update, context):
    """When list is hit"""
    update.message.reply_text(' 1)Power system \n 2)Machines \n 3)Power Electronics \n 4)Network \n 5)Control System \n 6)EMFT \n 7)Signal and System \n 8)Analog Electronics \n 9)Digital Electronics \n 10)Measurements \n 11)Materials\n 12)Communication System \n 13)Microprocessor \n 14)Mathematics')

def Power_system(update, context):
   """When /1 is hit"""
   update.message.reply_text('https://drive.google.com/file/d/1D2AigSJW1xFTNUUS6FBsaRd7bgZys9NJ/view?usp=sharing')

def Machines(update, context):
   """When /2 is hit"""
   update.message.reply_text('https://drive.google.com/file/d/1N3NGdXMKs5az11Pw5YSABwm7xL1rvepK/view?usp=sharing')

def Power_Electronics(update, context):
   """When /3 is hit"""
   update.message.reply_text('https://drive.google.com/file/d/1a7qqu5fIbBmLZpz9ejNefONqnIRPlFh3/view?usp=sharing')

def Network(update, context):
   """When /4 is hit"""
   update.message.reply_text('https://drive.google.com/file/d/13DmYvq6qdGVffRFdbRu3-jnknj63p-zj/view?usp=sharing')

def Control_system(update, context):
   """When /5 is hit"""
   update.message.reply_text('https://drive.google.com/file/d/10lWMn9aC-5WPdwIem3_SEtGbjncF0rLw/view?usp=sharing')

def EMFT(update, context):
   """When /6 is hit"""
   update.message.reply_text('https://drive.google.com/file/d/1rt0W2yJe9Msexy7GAIay3PkWxNgKWCes/view?usp=sharing')

def Signal(update, context):
   """When /7 is hit"""
   update.message.reply_text('https://drive.google.com/file/d/1yStT4O2BhbmMXgnL-2q7QwBmAn8_gIL6/view?usp=sharing')

def Analog(update, context):
   """When /8 is hit"""
   update.message.reply_text('https://drive.google.com/file/d/1YVyvNBsv0BhgNU-Xt4k6Rto_xYh0APr3/view?usp=sharing')

def Digital(update, context):
   """When /9 is hit"""
   update.message.reply_text('https://drive.google.com/file/d/1Z33DOz8T3FQXx6ded_wvE-ptCe2g9-ml/view?usp=sharing')

def Measurements(update, context):
   """When /10 is hit"""
   update.message.reply_text('https://drive.google.com/file/d/1pr_ftuVAst08Xd8TWRR21r2b5eGG9Fkb/view?usp=sharing')

def Materials(update, context):
   """When /11 is hit"""
   update.message.reply_text('https://drive.google.com/file/d/1OKZ9GrWkd1tX2BLD7q4mQdrDtkzlGMX9/view?usp=sharing')

def Communication(update, context):
   """When /12 is hit"""
   update.message.reply_text('https://drive.google.com/file/d/1xT22GOTnGiU9Yoaf3SILa_piyloxnuW9/view?usp=sharing')

def Microprocessor(update, context):
   """When /13 is hit"""
   update.message.reply_text('https://drive.google.com/file/d/1oArlhP1ghM67uR1HdFl89XOprpiBZTcr/view?usp=sharing')

def Maths(update, context):
   """When /14 is hit"""
   update.message.reply_text('https://drive.google.com/file/d/1syJZ5KMnzqdn4e9EN35K9Ip0wbMQZJIL/view?usp=sharing')

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
    dp.add_handler(CommandHandler("list",subject_list))
    dp.add_handler(CommandHandler("1",Power_system))
    dp.add_handler(CommandHandler("2",Machines))
    dp.add_handler(CommandHandler("3",Power_Electronics))
    dp.add_handler(CommandHandler("4",Network))
    dp.add_handler(CommandHandler("5",Control_system))
    dp.add_handler(CommandHandler("6",EMFT))
    dp.add_handler(CommandHandler("7",Signal))
    dp.add_handler(CommandHandler("8",Analog))
    dp.add_handler(CommandHandler("9",Digital))
    dp.add_handler(CommandHandler("10",Measurements))
    dp.add_handler(CommandHandler("11",Materials))
    dp.add_handler(CommandHandler("12",Communication))
    dp.add_handler(CommandHandler("13",Microprocessor))
    dp.add_handler(CommandHandler("14",Maths))
    #registering Message Handler to reply to user
    #starting the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
   main()