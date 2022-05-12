import telebot
import time

from telebot import types

bot = telebot.TeleBot("5146685537:AAHABy4_CfdgdeLPzE8W4yE7NL9EwwdS938")


@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Let's start📝")
    markup.add(item1)

    sti = open('images/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, "Привет дорогой, {0.first_name}!\n"
                                      "Я <b>{1.first_name}</b>, бот который, поможет"
                                      "не забыть о важных вещах и напоминать вам преждевременно "
                                      "такие вещи как оплата за Коммуналку, Электричество, Воду и Кредиты"
                                      "\nНажмите на кнопку <b>Lets start</b> и начинайте пользоваться ботом )"
                     .format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.chat.type == 'private':
        if message.text == 'English🇺🇸':
            markup_reply_english = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton(text='Communal')
            btn2 = types.KeyboardButton(text='Electricity')
            btn3 = types.KeyboardButton(text='Water')
            btn4 = types.KeyboardButton(text='Credit')
            markup_reply_english.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id,
                             'Okay, choose what you need:', reply_markup=markup_reply_english)

        elif message.text == 'Russian🇷🇺':
            markup_reply_russian = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton(text='Коммуналка')
            btn2 = types.KeyboardButton(text='Свет')
            btn3 = types.KeyboardButton(text='Вода')
            btn4 = types.KeyboardButton(text='Кредит')
            markup_reply_russian.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id,
                             'Окей, выберите то что вам нужно:', reply_markup=markup_reply_russian)

        elif message.text == 'Kazakh🇰🇿':
            markup_reply_russian = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton(text='Коммуналдық')
            btn2 = types.KeyboardButton(text='Жарық')
            btn3 = types.KeyboardButton(text='Су')
            btn4 = types.KeyboardButton(text='Несие')
            markup_reply_russian.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id,
                             'Жарайды, қажет нәрсені таңдаңыз:', reply_markup=markup_reply_russian)

        if message.text == "Let's start📝":
            markup_wel = types.ReplyKeyboardMarkup(resize_keyboard=True)
            lang1 = types.KeyboardButton(text="English🇺🇸")
            lang2 = types.KeyboardButton(text="Russian🇷🇺")
            lang3 = types.KeyboardButton(text="Kazakh🇰🇿")
            markup_wel.add(lang1, lang2, lang3)
            bot.send_message(message.chat.id, 'Choose a language that suits you:', reply_markup=markup_wel)

        if message.text == "30s":
            time.sleep(30)
            bot.send_message(message.chat.id, "I wanted to notify you that 30 seconds have passed")

        if message.text == "60s":
            time.sleep(60)
            bot.send_message(message.chat.id, "I wanted to notify you that 60 seconds have passed")

        if message.text == "30c":
            time.sleep(30)
            bot.send_message(message.chat.id, "Я хотел сообщить вам, что уже прошло 30 секунд")

        if message.text == "60c":
            time.sleep(60)
            bot.send_message(message.chat.id, "Я хотел сообщить вам, что уже прошло 60 секунд")

        if message.text == "30":
            time.sleep(30)
            bot.send_message(message.chat.id, "Мен сізге 30 секунд өткенін хабарлағым келді")

        if message.text == "60":
            time.sleep(60)
            bot.send_message(message.chat.id, "Мен сізге 60 секунд өткенін хабарлағым келді")

        if message.text == "Enter amount":
            bot.register_next_step_handler(message, credit_sum_en)

        if message.text == "Ввести сумму":
            bot.register_next_step_handler(message, credit_sum_ru)

        if message.text == "Соманы енгізіңіз":
            bot.register_next_step_handler(message, credit_sum_kz)

        if message.text == "Communal":
            photo = open('images/communal.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            markup_set_time = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton(text='30s')
            btn2 = types.KeyboardButton(text='60s')
            markup_set_time.add(btn1, btn2)
            bot.send_message(message.chat.id, "Okay, you have chosen a communal apartment!"
                                              "\nChoose a time to remind you", reply_markup=markup_set_time)

        if message.text == "Electricity":
            markup_set_time = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton(text='30s')
            btn2 = types.KeyboardButton(text='60s')
            markup_set_time.add(btn1, btn2)
            photo = open('images/electricity.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Okay, you chose the light! 💡 "
                                              "\nChoose a time to remind you", reply_markup=markup_set_time)

        if message.text == "Water":
            markup_set_time = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton(text='30s')
            btn2 = types.KeyboardButton(text='60s')
            markup_set_time.add(btn1, btn2)
            photo = open('images/water.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Okay, you chose water! 💧"
                                              "\nChoose a time to be reminded", reply_markup=markup_set_time)

        if message.text == "Credit":
            markup_set_time = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton(text='30s')
            btn2 = types.KeyboardButton(text='60s')
            btn3 = types.KeyboardButton(text='Enter amount')
            markup_set_time.add(btn1, btn2, btn3)
            photo = open('images/credit.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Okay you choose Credit!\n"
                                              "Choose a time to be reminded "
                                              "or select 'Enter amount' "
                                              "and we will calculate for you, how much do you need to "
                                              "pay for a month!", reply_markup=markup_set_time)
        # if Russian is selected
        if message.text == "Коммуналка":
            markup_set_time = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton(text='30c')
            btn2 = types.KeyboardButton(text='60c')
            markup_set_time.add(btn1, btn2)
            photo = open('images/communal.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Окей, вы выбрали коммуналку!"
                                              "\nВыберите время когда вам напомнить", reply_markup=markup_set_time)

        if message.text == "Свет":
            markup_set_time = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton(text='30c')
            btn2 = types.KeyboardButton(text='60c')
            markup_set_time.add(btn1, btn2)
            photo = open('images/electricity.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Окей, вы выбрали свет! 💡"
                                              "\nВыберите время когда вам напомнить", reply_markup=markup_set_time)

        if message.text == "Вода":
            markup_set_time = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton(text='30c')
            btn2 = types.KeyboardButton(text='60c')
            markup_set_time.add(btn1, btn2)
            photo = open('images/water.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Окей, вы выбрали воду! 💧"
                                              "\nВыберите время когда вам напомнить", reply_markup=markup_set_time)

        if message.text == "Кредит":
            markup_set_time = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton(text='30c')
            btn2 = types.KeyboardButton(text='60c')
            btn3 = types.KeyboardButton(text='Ввести сумму')
            markup_set_time.add(btn1, btn2, btn3)
            photo = open('images/credit.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Окей, вы выбрали кредит"
                                              "\nВыберите время когда вам напомнить "
                                              "или же выбрите 'Ввести сумму' И мы вам посчитаем, "
                                              "сколько вам надо будет "
                                              "оплачивать за месяц!", reply_markup=markup_set_time)
        # if Kazakh is selected
        if message.text == "Коммуналдық":
            markup_set_time = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton(text='30')
            btn2 = types.KeyboardButton(text='60')
            markup_set_time.add(btn1, btn2)
            photo = open('images/communal.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Жарайды, сіз коммуналдық услуга таңдадыңыз!"
                                              "\nЕске салатын уақытты таңдаңыз", reply_markup=markup_set_time)

        if message.text == "Жарық":
            markup_set_time = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton(text='30')
            btn2 = types.KeyboardButton(text='60')
            markup_set_time.add(btn1, btn2)
            photo = open('images/electricity.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Жарайды, сіз жарықты таңдадыңыз! 💡"
                                              "\nЕске салатын уақытты таңдаңыз", reply_markup=markup_set_time)

        if message.text == "Су":
            markup_set_time = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton(text='30')
            btn2 = types.KeyboardButton(text='60')
            markup_set_time.add(btn1, btn2)
            photo = open('images/water.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Жарайды, сіз суды таңдадыңыз! 💧"
                                              "\nЕске салатын уақытты таңдаңыз", reply_markup=markup_set_time)

        if message.text == "Несие":
            markup_set_time = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton(text='30')
            btn2 = types.KeyboardButton(text='60')
            btn3 = types.KeyboardButton(text='Соманы енгізіңіз')
            markup_set_time.add(btn1, btn2, btn3)
            photo = open('images/credit.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Жарайды, сіз Несие таңдадыңыз!\n"
                                              "Еске салатын уақытты таңдаңыз "
                                              "немесе «Соманы енгізу» таңдаңыз, "
                                              "сонда біз сіз үшін есептейміз, "
                                              "сізге қанша керектігін бір айға төлеуге!", reply_markup=markup_set_time)


def credit_sum_en(message):
    sum = int(message.text)
    month = 12
    res = sum / month
    bot.send_message(message.chat.id, "We calculated, so you have to pay " + str(res) +
                     ", to pay for everything in 1 year!")


def credit_sum_ru(message):
    sum = int(message.text)
    month = 12
    res = sum / month
    bot.send_message(message.chat.id, "Мы посчитали, значит вам придется оплачивать " + str(res) +
                     ", чтобы оплатить все за 1 год!")


def credit_sum_kz(message):
    sum = int(message.text)
    month = 12
    res = sum / month
    bot.send_message(message.chat.id, "Біз есептедік, сіз төлеуіңіз керек " + str(res) +
                     ", бәрін 1 жылда төлеу ушин!")


# RUN
bot.polling(none_stop=True, interval=0)
