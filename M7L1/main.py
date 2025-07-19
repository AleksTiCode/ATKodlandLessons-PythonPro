import os
from dotenv import load_dotenv
import telebot
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
from neyronka import func

load_dotenv()
TG_TOKEN = os.getenv('TG_TOKEN')

bot = telebot.TeleBot(TG_TOKEN)



@bot.message_handler(commands=['start'])
def start_command(message):
    text = (
        f'Привет, {message.from_user.first_name}!👋\n\n'
        'Я бот, который умеет распознавать объект на фото🖼️\n'
        'Отправь мне фотографию, а я скажу, что на ней изображено🤓'
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        temp_message = bot.reply_to(message, 'Идёт обработка...')
        file_info = bot.get_file(message.photo[-1].file_id)
        file_name = file_info.file_path.split('/')[-1]

        # downloaded_file = bot.download_file(file_info.file_path)
        with open(f'images/{file_name}', 'wb') as file:
            file.write(bot.download_file(file_info.file_path))

        agent, sposobki = func(file_name)

        bot.delete_message(temp_message.chat.id, temp_message.id)
        bot.reply_to(message, f'Агент {agent}\nСпособности: {", ".join(sposobki)}')
        os.remove(f'images/{file_name}')
    except Exception as e:
        bot.reply_to(message, 'Произошла ошибка при обработке фотографии.')
        print(e)

bot.infinity_polling()