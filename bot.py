import logging
from emoji import emojize
from glob import glob
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import choice

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

# PROXY = {'proxy_url': settings.PROXY_URL,
#     'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def get_smile(user_data):
    if 'emoji' not in user_data:      
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, language='alias')
    return user_data['emoji']

def greet_user(update, context):
    print("Вызван /start")
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f"Здравствуй пользователь {context.user_data['emoji']}")

def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    username = update.effective_user.first_name
    text = update.message.text
    print(text)
    update.message.reply_text(f"{username} {context.user_data['emoji']}, ты написал(а) мне: {text}")

def send_image(update, context):
    img_list = glob("images/*.jp*g")
    img_filename = choice(img_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(img_filename, 'rb'))

def main():
    mybot = Updater(settings.API_KEY, use_context=True)    # <--- request_kwargs=PROXY

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("images", send_image))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()
