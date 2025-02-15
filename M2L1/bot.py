import telebot, os, random, requests
from config import *
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = ReplyKeyboardMarkup()
    button_1 = KeyboardButton('/meme')
    button_2 = KeyboardButton('/duck')
    keyboard.add(button_1)
    keyboard.add(button_2)
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!', reply_markup=keyboard)

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

@bot.message_handler(commands=['duck'])
def duck_func(message):
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    
    bot.reply_to(message, data['url'])

bot.infinity_polling()