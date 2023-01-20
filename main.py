import time
from datetime import datetime
from datetime import date
import telebot
from telebot import types
from config import TOKEN

sultan = telebot.TeleBot(token=TOKEN)

def get_markup():
    markup = types.ReplyKeyboardMarkup(row_width=3)
    itembtn1 = types.KeyboardButton('Салам')
    itembtn2 = types.KeyboardButton('Cаaт канча болду?')
    itembtn3 = types.KeyboardButton('Датаны корсот.')
    itembtn4 = types.KeyboardButton('Атын ким?')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    return markup

def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def get_date():
    return date.today()

@sultan.message_handler(content_types=['text'])
def answer_the_message(message):

    help_msg = 'жардам'
    ans_help = 'Кандай жардам алууну каалайсыз? 😊'
    time_msg = 'Cаaт канча болду?'
    hello_msg = 'Салам'
    hi_msg = 'Уаллейкум ассалам'
    date_msg = 'Датаны корсот.'
    name_bot = 'Менин атым Султан.'

    if message.text == 'Атын ким?':
        sultan.send_message(message.chat.id, name_bot)

    elif message.text.lower() == help_msg:
        sultan.send_message(message.chat.id,ans_help,reply_markup=get_markup())

    elif message.text == time_msg:
        sultan.send_message(message.chat.id, get_time())

    elif message.text == hello_msg:
        sultan.send_message(message.chat.id, hi_msg)

    elif message.text == date_msg:
        sultan.send_message(message.chat.id, get_date())

    else:
        sultan.send_message(message.chat.id, 'Сроону туура бериниз')


sultan.infinity_polling()