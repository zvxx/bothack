import env

import telebot

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = env.BOT_TOKEN

bot = telebot.TeleBot(TOKEN)

START = """

<strong>

- Just send a Repo Link ...

- Example:</strong> <code>https://github.com/TelegramBot/Api</code>

"""

@bot.message_handler(commands=['start'])

def start(message):

    text = START

    buttons = InlineKeyboardMarkup()

    a = InlineKeyboardButton("Dev", url="t.me/u_r_r")

    buttons.add(a)

    bot.send_message(

        message.chat.id,

        text,

        reply_markup=buttons,

        parse_mode='html',

        disable_web_page_preview=True

    )

@bot.message_handler(content_types=['text'])

def github(message):

    if 'github.com' not in message.text:

        bot.send_message(message.chat.id, "Error Url", reply_to_message_id=message.id)

    else:

        try:

            doc = f'{message.text}/archive/master.zip'

            bot.send_document(

                message.chat.id,

                document=doc,

                caption=f'Successfully Downloaded\n\n The Url : <code>{message.text}</code>',

                reply_to_message_id=message.id,

                parse_mode='html'

            )

        except Exception as e:

            print(e)

            bot.reply_to(message, "Error Repo Link")

bot.infinity_polling()
