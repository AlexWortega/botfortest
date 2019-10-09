import telebot
import cv2
import argparse

bot = telebot.TeleBot('968559605:AAE1YTitg7QxUj-IrcgGivVRXd39AQW7aPI')

def kiski_detection():
    image = cv2.imread('exmpl.jpg')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я помогу отличить кота от хлеба! Объект перед тобой квадратный?')
@bot.message_handler(content_types=['images'])
def piski(message):
    print("gg")
    bot.send_photo(message.from_user.id,'https://opencv-python-tutroals.readthedocs.io/en/latest/_images/face.jpg')
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text.upper()  == "ДА":
        bot.send_message(message.from_user.id, "У него есть уши?")
        bot.send_photo(message.from_user.id, 'https://opencv-python-tutroals.readthedocs.io/en/latest/_images/face.jpg')
        message.text = None
        if message.text.upper == "ДА":
            bot.send_message(message.from_user.id, "Это кот  а не хлеб мудило")

        elif message.text.upper() == "НЕТ":
            bot.send_message(message.from_user.id, "Нет, ты реально не отличаешь хлеб от кота? Ешь его!")


    elif message.text.upper() == "НЕТ":
        bot.send_message(message.from_user.id, "Это кот а не злеб ешь его")

bot.polling()
