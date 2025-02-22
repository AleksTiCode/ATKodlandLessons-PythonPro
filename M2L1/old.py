# import telebot, os, random, requests
# from config import *
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton
# from dotenv import load_dotenv

# load_dotenv("./.env")

# bot = telebot.TeleBot(os.getenv("TOKEN"))

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     keyboard = ReplyKeyboardMarkup()
#     button_1 = KeyboardButton('/meme dev')
#     button_2 = KeyboardButton('/meme animal')
#     button_3 = KeyboardButton('/meme random')
#     keyboard.add(button_1)
#     keyboard.add(button_2)
#     keyboard.add(button_3)
#     bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!', reply_markup=keyboard)

# @bot.message_handler(commands=['meme'])
# def send_meme(message):
#     global rarely_dev, rarely_animal, last_meme_dev, last_meme_animal
#     arg = telebot.util.extract_arguments(message.text)
#     # global last_img
#     # if last_img == 5:
#     #     last_img = 0
#     # with open(f'M2L1\\images\\img{last_img+1}.png', 'rb') as file:
#     #     file = file.read()
#     # last_img += 1

#     if arg == 'dev':
#         img = random.choice(os.listdir('M2L1\\images\\dev'))
#         caption = 'Обычный мем'
#         if img == 'img5.png' and rarely_dev != 3:
#                 last_meme_dev = img
#                 rarely_dev += 1
#         elif img == 'img5.png' and rarely_dev == 3:
#             rarely_dev = 0
#             caption = 'Редкий мем'
#         while img == last_meme_dev:
#             img = random.choice(os.listdir('M2L1\\images\\dev'))
#             if img == 'img5.png' and rarely_dev != 3:
#                 last_meme_dev = img
#                 rarely_dev += 1
#         with open(f'M2L1\\images\\dev\\{img}', 'rb') as file:
#             file = file.read()
#         bot.send_photo(message.chat.id, file, caption=caption)
#         last_meme_dev = img

#     elif arg == 'animal':
#         img = random.choice(os.listdir('M2L1\\images\\animal'))
#         caption = 'Обычный мем'
#         if img == 'img5.png' and rarely_animal != 3:
#             last_meme_animal = img
#             rarely_animal += 1
#         elif img == 'img5.png' and rarely_animal == 3:
#             rarely_animal = 0
#             caption = 'Редкий мем'
#         while img == last_meme_animal:
#             img = random.choice(os.listdir('M2L1\\images\\dev'))
#             if img == 'img5.png' and rarely_animal != 3:
#                 last_meme_animal = img
#                 rarely_animal += 1
#         with open(f'M2L1\\images\\animal\\{img}', 'rb') as file:
#             file = file.read()
#         bot.send_photo(message.chat.id, file, caption=caption)
#         last_meme_animal = img

#     else:
#         url = 'https://random-d.uk/api/random'
#         res = requests.get(url)
#         data = res.json()
        
#         bot.reply_to(message, data['url'])

# @bot.message_handler(commands=['duck'])
# def duck_func(message):
#     url = 'https://random-d.uk/api/random'
#     res = requests.get(url)
#     data = res.json()
    
#     bot.reply_to(message, data['url'])

# bot.infinity_polling()