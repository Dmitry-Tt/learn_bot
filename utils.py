from emoji import emojize
from random import choice
from telegram import ReplyKeyboardMarkup, KeyboardButton

import settings


def get_smile(user_data):
    if 'emoji' not in user_data:      
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, language='alias')
    return user_data['emoji']

def main_keyboard():
    return ReplyKeyboardMarkup([['Картинка', KeyboardButton('Мое местоположение', request_location=True)]], resize_keyboard=True)
