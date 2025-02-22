import telebot, os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv("./.env")

bot = telebot.TeleBot(os.getenv("TOKEN"))

def keyboard_func():
  keyboard = InlineKeyboardMarkup()
  keyboard.add(InlineKeyboardButton("paper", callback_data="paper"))
  keyboard.add(InlineKeyboardButton("glass", callback_data="glass"))
  keyboard.add(InlineKeyboardButton("plastic", callback_data="plastic"))
  keyboard.add(InlineKeyboardButton("foil", callback_data="foil"))
  keyboard.add(InlineKeyboardButton("meat", callback_data="meat"))
  return keyboard

@bot.message_handler(commands=['start', 'help'])
def start_func(message):
  bot.reply_to(message, "Привет, я Эко-бот")

@bot.message_handler(commands=["eco"])
def eco_func(message):
  bot.send_message(message.chat.id, "Для какого предмета хочешь узнать срок разложения", reply_markup=keyboard_func())

@bot.callback_query_handler(func=lambda call: call.data in ["paper", "glass", "plastic", "foil", "meat"])
def buttons_func(call):
  eco_list = {"paper": "от двух дней до двух лет",
              "glass": "более 1000 лет (почти не разлагается)",
              "plastic": "более 600 лет",
              "foil": "более 100 лет",
              "meat": "от 1 месяца"}
  bot.answer_callback_query(call.id)
  bot.send_message(call.message.chat.id, f"Время разложения: {eco_list[call.data]}")

bot.infinity_polling()