import telebot, os, random
from config import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

@bot.message_handler(commands=['meme'])
def send_meme(message):
    global last_meme
    # global last_img
    # if last_img == 5:
    #     last_img = 0
    # with open(f'M2L1\\images\\img{last_img+1}.png', 'rb') as file:
    #     file = file.read()
    # last_img += 1

    img = random.choice(os.listdir('M2L1\\images'))
    while img == last_meme:
        img = random.choice(os.listdir('M2L1\\images'))
    with open(f'M2L1\\images\\{img}', 'rb') as file:
        file = file.read()
    last_meme = img
    bot.send_photo(message.chat.id, file)

bot.infinity_polling()