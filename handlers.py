from glob import glob
from random import choice

from utils import get_smile, main_keyboard

def greet_user(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(
        f"Здравствуй пользователь {context.user_data['emoji']}", 
        reply_markup=main_keyboard()
    )

def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    username = update.effective_user.first_name
    text = update.message.text
    print(text)
    update.message.reply_text(
        f"{username} {context.user_data['emoji']}, ты написал(а) мне: {text}",
        reply_markup=main_keyboard()
    )

def send_image(update, context):
    img_list = glob("images/*.jp*g")
    img_filename = choice(img_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(
        chat_id=chat_id, photo=open(img_filename, 'rb'), 
        reply_markup=main_keyboard()
    )

def user_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(
        f"Ваши координаты {coords} {context.user_data['emoji']}",
        reply_markup=main_keyboard()
    )
