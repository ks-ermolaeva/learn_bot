from glob import glob
from random import choice

from utiles import get_smile, play_random_numbers, main_keyboard


def greet_user(update, context):
    print('Вызван /start')
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(
        f'Привет! Это Learn Python Mega Bot {context.user_data["emoji"]}',
        reply_markup=main_keyboard()
    )


def guess_number(update, context):
    print(context.args)
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
            message = "Введите целое число"
    else:
        message = "Введите число"
    update.message.reply_text(message, reply_markup=main_keyboard())


def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    text = update.message.text
    print(text)
    update.message.reply_text(
        f'{text} {context.user_data["emoji"]}',
        reply_markup=main_keyboard()
    )


def send_vk_photo(update, context):
    vk_photo_list = glob('images/vk*.jp*g')
    vk_photo_filename = choice(vk_photo_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(vk_photo_filename, 'rb'), reply_markup=main_keyboard())


def user_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(
        f"Ваши координаты {coords} {context.user_data['emoji']}",
        reply_markup=main_keyboard()
    )
