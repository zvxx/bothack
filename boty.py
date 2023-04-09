import os
import telebot
import json
import requests
import time
from telebot import types
from telebot.types import Message
from StringSessionBot.database import SESSION
from StringSessionBot.database.users_sql import Users, num_users

@bot.message_handler(func=lambda msg: True, content_types=["text"])
def users_sql(msg: Message):
    if msg.from_user:
        q = SESSION.query(Users).get(int(msg.from_user.id))
        if not q:
            SESSION.add(Users(msg.from_user.id))
            SESSION.commit()
        else:
            SESSION.close()


@bot.message_handler(commands=['stats'])
def _stats(msg: Message):
    users = num_users()
    bot.reply_to(msg, f"Total Users : {users}")



url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'

bot = telebot.TeleBot('6013707265:AAEVh6Sd4YR_L57fQpK5Lqgy_5HOeyM3YZI')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    name = message.from_user.first_name
    Let_mark = types.InlineKeyboardMarkup()
    rL = types.InlineKeyboardButton("- الـمـطوࢪ . ", url="t.me/u_r_r")
    help_button = types.InlineKeyboardButton("- طـريقـة الاسـتخـدام؟ . ", callback_data="help")
    Let_mark.row(help_button)
    Let_mark.add(rL)
    bot.reply_to(message, f'''*
- Welcome {name}

❖ - This is an artificial intelligence bot You can ask it any question and it will answer you regardless of whether it is software or general Click on the 'method of use' to know the features of the bot.

❖ - هـذه بـوت ذكـاء اسـطـناعـي يـمـكنـك سـأله آي سـؤال ويـرد عـليـك مـهما كـان بـرمجـي او عـام اضـغط عـلى 'طـريـقـة الاستـخـدام' لمعرفة مميزات البوت.
*''', parse_mode='Markdown', reply_markup=Let_mark)

@bot.callback_query_handler(func=lambda call: call.data == "help")
def send_help(call):
    help_message = f'''
*- هــذه هـي قـائـمة اسـتـخـدامـي .*

*- هالاوامــئ الـمـتـوفـرة حـالـيًا .*

/Levi - لـلـسؤال آي سـؤال بالـذكـاء الاسـطـناعي
*مـثـال :
ما هيه اكبر ساعه في العالم Levi/
*

/LeVo - لـتحـويل الـكـلام الـى صـوت
*مـثـال :
/LeVo السلام عليكم 
*'''

    back_button = types.InlineKeyboardButton("- الـࢪجـوع . ", callback_data="back")
    keyboard = types.InlineKeyboardMarkup().add(back_button)
    bot.send_message(call.message.chat.id, help_message, reply_markup=keyboard, parse_mode='Markdown')

@bot.callback_query_handler(func=lambda call: call.data == "back")
def send_welcome_back(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    bot.delete_message(chat_id, message_id-1)
    send_welcome(call.message)
    bot.delete_message(chat_id, message_id-0)




@bot.message_handler(commands=['LeVo'])
def Levo(message):
   try:
   	Leoo = message.text.replace('/LeVo', '', 1)
   	if not Leoo:
   		bot.reply_to(message, "- Please include your prompt after the /LeVo the Talk  .\n\n- الـࢪجـاء وضـع الـكلام بـعـد امـࢪ /LeVo .")
   	urlt = f'http://translate.google.com/translate_tts?q={Leoo}&tl=ar&client=duncan3dc-speaker'
   	bot.send_voice(message.chat.id,urlt,f'''- Finish .\n\n<b><u>Dev : Levi = ' @u_r_r '</u></b>''',parse_mode="HTML",reply_to_message_id=message.message_id)
   	
   	if 'LeVo' not in message.text:
   		bot.reply_to(message, "- Please include your prompt after the /LeVo the Talk  .\n\n- الـࢪجـاء وضـع الـكلام بـعـد امـࢪ /LeVo .")
   except:
   	bot.reply_to(message, "- Error generating the Voice Please try again or not speaking  .\n\n- خـطـأ فـي صـنـع الـرساله الصـوتـيه حـاول مـࢪة اخـرى او غـيࢪ الكـلام . ")


def gpt(text) -> str:
    headers = {
        'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
        'Connection': 'keep-alive',
        'If-None-Match': 'W/"1c3-Up2QpuBs2+QUjJl/C9nteIBUa00"',
        'Accept': '*/*',
        'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/15.6.1 hw/iPhone8_2',
        'Content-Type': 'application/json',
        'Accept-Language': 'en-GB,en;q=0.9'
    }

    data = {
        'data': {
            'message':text,
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    try:
        result = response.json()["result"]["choices"][0]["text"]
        return result
    except:
        return None

@bot.message_handler(commands=['Levi'])
def Lev(message):
    prompt = message.text.replace('/Levi', '', 1)
    if not prompt:
        bot.reply_to(message, "- Please include your prompt after the /Levi command .\n\n- الـࢪجـاء وضـع الطـلب بـعـد امـࢪ /Levi .")
        return
    try:
        code = gpt(prompt)
        code = code.replace("<?php", "")
        bot.reply_to(message, f"<u>Your requested :\n</u> \n<b>{code}</b>\n\n<u>Dev : Levi = ' @u_r_r '</u>", parse_mode='HTML')
    except:
        bot.reply_to(message, "- Error generating code Please try again .\n\n- خـطـأ فـي صـنـع الـكـود حـاول مـࢪة اخـرى .")

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    if 'Levi' not in message.text:
        bot.reply_to(message, "Please include the word /Levi before your order .\n\n- الـࢪجـاء وضـع امـࢪ /Levi قـبل طـلـبك .")
    elif message.text.strip().lower() == 'levi':
        bot.reply_to(message, "- Please use the command /Levi followed by your prompt .\n\n- الـࢪجاء اسـتـخدام امـࢪ /Levi قـبـل طـلـبك .")
    else:
        Lev(message)

@bot.message_handler(func=lambda message: message.chat.type == 'group', commands=['Levi'])
def Lev_group(message):
    prompt = message.text.replace('/Levi', '', 1)
    if not prompt:
        bot.reply_to(message, "- Please include your prompt after the /Levi command .\n\n- الـࢪجـاء وضـع طـلب بـعد امـࢪ /Levi .")
        return
    try:
        code = gpt(prompt)
        code = code.replace("<?php", "")
        bot.reply_to(message, f"<u>Your requested :\n</u> \n<b>{code}</b>\n\n<u>Dev : Levi = ' @u_r_r '</u>", parse_mode='HTML')
    except:
        pass

@bot.message_handler(commands=['LeVo'])
def Levo(message):
   try:
   	Leoo = message.text.replace('/LeVo', '', 1)
   	if not Leoo:
   		bot.reply_to(message, "- Please include your prompt after the /LeVo the Talk  .\n\n- الـࢪجـاء وضـع الـكلام بـعـد امـࢪ /Levi .")
   	urlt = f'http://translate.google.com/translate_tts?q={Leoo}&tl=ar&client=duncan3dc-speaker'
   	bot.send_voice(message.chat.id,urlt,f'''- Finish .\n\n<b><u>Dev : Levi = ' @u_r_r '</u></b>''',parse_mode="HTML",reply_to_message_id=message.message_id)
   	
   	if 'LeVo' not in message.text:
   		bot.reply_to(message, "- Please include your prompt after the /LeVo the Talk  .\n\n- الـࢪجـاء وضـع الـكلام بـعـد امـࢪ /LeVo .")
   except:
   	bot.reply_to(message, "- Error generating the Voice Please try again or not speaking  .\n\n- خـطـأ فـي صـنـع الـرساله الصـوتـيه حـاول مـࢪة اخـرى او غـيࢪ الكـلام . ")

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text.strip().lower() == 'levi':
        bot.reply_to(message, "- Please use the command /Levi followed by your prompt .\n\n- الـࢪجاء اسـتـخدام امـࢪ /Levi قـبـل طـلـبك .")
    else:
        Lev_group(message)

bot.polling()
