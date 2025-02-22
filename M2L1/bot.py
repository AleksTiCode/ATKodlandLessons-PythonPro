import telebot, os, random, requests
from config import *
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

load_dotenv("./.env")

bot = telebot.TeleBot(os.getenv("TOKEN"))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = ReplyKeyboardMarkup()
    button_1 = KeyboardButton('/meme dev')
    button_2 = KeyboardButton('/meme animal')
    button_3 = KeyboardButton('/meme random')
    keyboard.add(button_1)
    keyboard.add(button_2)
    keyboard.add(button_3)
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!', reply_markup=keyboard)

@bot.message_handler(commands=['meme'])
def send_meme(message):
    global rarely_dev, rarely_animal, last_meme_dev, last_meme_animal
    arg = telebot.util.extract_arguments(message.text)

    num = random.choice([1,1,2,2,3,3,4,4,5])
    if arg == 'dev':
        while num == last_meme_dev:
            num = random.choice([1,1,2,2,3,3,4,4,5])
        if num == 5:
            caption = 'Редкий мем'
        else:
            caption = 'Обычный мем'
        with open(f'M2L1\\images\\dev\\img{num}.png', 'rb') as file:
            file = file.read()
        bot.send_photo(message.chat.id, file, caption=caption)
        last_meme_dev = num

    elif arg == 'animal':
        while num == last_meme_animal:
            num = random.choice([1,1,2,2,3,3,4,4,5])
        if num == 5:
            caption = 'Редкий мем'
        else:
            caption = 'Обычный мем'
        with open(f'M2L1\\images\\animal\\img{num}.png', 'rb') as file:
            file = file.read()
        bot.send_photo(message.chat.id, file, caption=caption)
        last_meme_animal = num

    else:
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        
        bot.reply_to(message, data['url'])

@bot.message_handler(commands=['duck'])
def duck_func(message):
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    
    bot.reply_to(message, data['url'])

bot.infinity_polling()