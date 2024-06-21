from emoji import emojize
from random import choice, randint
from telegram import ReplyKeyboardMarkup, KeyboardButton

import settings


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile)
    return user_data['emoji']


def play_random_numbers(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f'Ваше число {user_number}, мое число {bot_number}. Поздравляю, вы выиграли!'
    elif user_number == bot_number:
        message = f'Ваше число {user_number}, мое число {bot_number}. Ничья :)'
    else:
        message = f'Ваше число {user_number}, мое число {bot_number}. Вы проиграли'
    return message


def main_keyboard():
    return ReplyKeyboardMarkup([['Посмотреть фото VK-Fest', KeyboardButton('Мои координаты', request_location=True)]])
