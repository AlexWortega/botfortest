import telebot
import cv2
import argparse

bot = telebot.TeleBot('968559605:AAE1YTitg7QxUj-IrcgGivVRXd39AQW7aPI')

def kiski_detection():
    image = cv2.imread('catpic.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # load the cat detector Haar cascade, then detect cat faces
    # in the input image
    detector = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
    rects = detector.detectMultiScale(gray, scaleFactor=1.3,
                                      minNeighbors=10, minSize=(75, 75))
    if len(rects) > 0:
        print('Debug : kiska detected')
    else:
        print('Debug : print kiska not detected')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я помогу отличить кота от хлеба! Объект перед тобой квадратный?')
<<<<<<< HEAD
@bot.message_handler(content_types=["photo"])
def piski(message):
    print("gg")
    bot.download_file(message.from_user.id)

=======
@bot.message_handler(content_types=['images'])
def recognize_kittens(message, image):
    print("gg")
    #тут будет распознование кисок
 #   bot.send_photo(message.from_user.id,'https://opencv-python-tutroals.readthedocs.io/en/latest/_images/face.jpg')
>>>>>>> c19e4941f415a5d48802728c62725ab3f1e83f00
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text.upper() == "ДА":
        bot.send_message(message.from_user.id, "У него есть уши?")
        bot.send_photo(message.from_user.id, 'https://opencv-python-tutroals.readthedocs.io/en/latest/_images/face.jpg')
        message.text = None
        if message.text.upper == "ДА":
            bot.send_message(message.from_user.id, "Это кот , а не хлеб не ешь его ")

        elif message.text.upper() == "НЕТ":
            bot.send_message(message.from_user.id, "Нет, ты реально не отличаешь хлеб от кота? Ешь его!")


    elif message.text.upper() == "НЕТ":
        bot.send_message(message.from_user.id, "Это кот а не хлеб ешь его")

bot.polling()
