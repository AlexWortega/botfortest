import telebot
import cv2
import argparse

bot = telebot.TeleBot('968559605:AAE1YTitg7QxUj-IrcgGivVRXd39AQW7aPI')

def kiski_detection():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="C:\Users\alexd\OneDrive\Desktop")
    ap.add_argument("-c", "--cascade",
                    default="haarcascade_frontalcatface_extended.xml",
                    help="path to cat detector haar cascade")
    args = vars(ap.parse_args())

    # load the input image and convert it to grayscale
    image = cv2.imread(args["image"])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # load the cat detector Haar cascade, then detect cat faces
    # in the input image
    detector = cv2.CascadeClassifier(args["cascade"])
    rects = detector.detectMultiScale(gray, scaleFactor=1.3,
                                      minNeighbors=10, minSize=(75, 75))

    # loop over the cat faces and draw a rectangle surrounding each
    for (i, (x, y, w, h)) in enumerate(rects):
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(image, "Cat #{}".format(i + 1), (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

    # show the detected cat faces
    cv2.imshow("Cat Faces", image)
    cv2.waitKey(0)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я помогу отличить кота от хлеба! Объект перед тобой квадратный?')

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text.upper()  == "ДА":
        bot.send_message(message.from_user.id, "У него есть уши?")
        message.text = None
        if message.text.upper == "ДА":
            bot.send_message(message.from_user.id, "Это кот  а не хлеб мудило")

        elif message.text.upper() == "НЕТ":
            bot.send_message(message.from_user.id, "Нет, ты реально не отличаешь хлеб от кота? Ешь его!")


    elif message.text.upper() == "НЕТ":
        bot.send_message(message.from_user.id, "Это кот а не злеб ешь его")

bot.polling()
