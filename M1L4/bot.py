import telebot
from config import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(content_types=['photo'])
def send_photo(message):
    file = bot.get_file(message.photo[-1].file_id)
    file_download = bot.download_file(file.file_path)
    file_path = 'M1L4\\images\\' + f'{message.photo[-1].file_id}.jpg'
    with open(file_path, 'wb') as file:
        file.write(file_download)
    bot.reply_to(message, "Если бы я умел видеть... Но я скачал!")

bot.infinity_polling()