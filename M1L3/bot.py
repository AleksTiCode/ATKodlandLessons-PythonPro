import telebot
from config import *
from logic import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Дарова.
Это бот, который делает ничего. но он нужен. ДА. Често не скопировано с документации. Честно-честно. \
""")
    
@bot.message_handler(commands=['create_pass'])
def create_pass(message):
    len_pass = telebot.util.extract_arguments(message.text)
    bot.send_message(message.chat.id, str(gen_pass(int(len_pass))))

@bot.message_handler(commands=['smile_pass'])
def create_pass(message):
    len_pass = telebot.util.extract_arguments(message.text)
    bot.send_message(message.chat.id, str(smile_pass(int(len_pass))))

# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)


bot.infinity_polling()