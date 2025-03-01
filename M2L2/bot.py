import telebot, os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from config import *

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

def keyboard_func_city():
  keyboard = InlineKeyboardMarkup()
  keyboard.add(InlineKeyboardButton("Люберцы", callback_data="Lubertsi"))
  keyboard.add(InlineKeyboardButton("Домодедово", callback_data="Domodedovo"))
  keyboard.add(InlineKeyboardButton("Видное", callback_data="Vidnoe"))
  return keyboard 

@bot.message_handler(commands=['start', 'help'])
def start_func(message):
  bot.reply_to(message, "Привет, я Эко-бот.\n Введи /eco, чтобы узнать сколько разлагаются некоторые виды материалов\n Введи /city, чтобы узнать местоположение пунктов переработки в поддерживаемых городах (на дыннй момент Люберцы, Домодедово и Видное) ")

@bot.message_handler(commands=["eco"])
def eco_func(message):
  bot.send_message(message.chat.id, "Для какого предмета хочешь узнать срок разложения", reply_markup=keyboard_func())

@bot.message_handler(commands=["city"])
def city_func(message):
  bot.send_message(message.chat.id, "Выбери город, в котором хочешь узнать пункты переработки", reply_markup=keyboard_func_city())

@bot.callback_query_handler(func=lambda call: call.data in ["paper", "glass", "plastic", "foil", "meat"])
def buttons_func(call):
  eco_list = {"paper": "от двух дней до двух лет",
              "glass": "более 1000 лет (почти не разлагается)",
              "plastic": "более 600 лет",
              "foil": "более 100 лет",
              "meat": "от 1 месяца"}
  bot.answer_callback_query(call.id)
  bot.send_message(call.message.chat.id, f"Время разложения: {eco_list[call.data]}")

@bot.callback_query_handler(func=lambda call: call.data in ["Lubertsi", "Domodedovo", "Vidnoe"])
def buttons_func(call):
  city_list = {"Lubertsi": Lubertsi,
              "Domodedovo": Domodedovo,
              "Vidnoe": Vidnoe}
  
  selected_city = city_list[call.data]
  bot.answer_callback_query(call.id)
  bot.send_message(call.message.chat.id, 
      f"Бумага: {selected_city['paper']}\n"
      f"Стекло: {selected_city['glass']}\n"
      f"Пластик: {selected_city['plastic']}\n"
      f"Металл: {selected_city['metal']}\n"
      f"Одежда: {selected_city['cloth']}\n"
      f"Лампочки: {selected_city['bulds']}\n"
      f"Крышки: {selected_city['caps']}\n"
      f"Техника: {selected_city['technique']}\n"
      f"Батарейки: {selected_city['batteries']}\n"
      f"Шины: {selected_city['tires']}\n"
      f"Опасное: {selected_city['danger']}")

bot.infinity_polling()