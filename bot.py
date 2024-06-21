import logging
from telegram.ext import (Updater, CommandHandler,
                          MessageHandler, Filters)

from handlers import (greet_user, guess_number, send_vk_photo,
                      user_coordinates, talk_to_me)

import settings

logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')


def main():
    mybot = Updater(settings.API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('guess', guess_number))
    dp.add_handler(CommandHandler('vk', send_vk_photo))
    dp.add_handler(MessageHandler(Filters.regex('^(Посмотреть фото VK-Fest)$'), send_vk_photo))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot started')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
