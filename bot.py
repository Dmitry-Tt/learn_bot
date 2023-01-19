import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings
from handlers import greet_user, send_image, talk_to_me, user_coordinates


logging.basicConfig(filename='bot.log', level=logging.INFO)

# PROXY = {'proxy_url': settings.PROXY_URL,
#     'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def main():
    mybot = Updater(settings.API_KEY, use_context=True)    # <--- request_kwargs=PROXY

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("images", send_image))
    dp.add_handler(MessageHandler(Filters.regex('^(Картинка)$'), send_image))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info('Bot started ...')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()
