import telebot,requests
from telebot import types

Token= ("6088451625:AAFQ9BFPAjy9Q6mBJrNjkZm7xjreU3u35B8") 
bot=telebot.TeleBot(Token)
telebot.logger.setLevel(__import__('logging').DEBUG)
@bot.message_handler(commands=["start"])
def Aa(message):
 id=message.chat.id
 name=message.chat.first_name
 user=message.from_user.username
 A=types.InlineKeyboardMarkup(row_width=2)
 B=types.InlineKeyboardButton("قناه المبرمج",url="https://t.me/CC22M")
 C=types.InlineKeyboardButton("المبرمج",url="https://t.me/CC22Y")
 D=types.InlineKeyboardButton("سحب سيشن  ايدي ",callback_data="insta")
 A.add(B,C,D)
 bot.send_message(message.chat.id,text="""
*➖ 👋اهلا عزيزي*  [{}](tg://settings/)
*في بوت سحب سشين ايدي انستكرام💫.*
*➖ ايدي :* [{}](tg://settings/)            
*➖ اليوزر :* @{} 
 """.format(name,id,user),parse_mode='markdown',reply_markup=A)
@bot.callback_query_handler(func=lambda call: True)
def c(call):
    if call.data == "insta":
        us = bot.reply_to(call.message,text="*ارسل حسابك ب نمط\n user:pass*",parse_mode='markdown')
        bot.register_next_step_handler(us,instaa)
def instaa(message):
 try:       
  username=message.text.split(':')[0]
  password=message.text.split(':')[1]
  print(username,password)
  url = "https://www.instagram.com/accounts/login/ajax/"
  cookies =""    
  headers ={
"accept": "*/*",
"set-cookie":"csrftoken=RfrLPLyTlkMfwpamAJ0ORu3F4GufRMzP; Domain=.instagram.com; expires=Mon, 16-Jan-2023 13:05:57 GMT; Max-Age=31449600; Path=/; Secure",
"accept-encoding":"gzip, deflate, br",
"accept-language":"fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
"content-length": "321",
"content-type": "application/x-www-form-urlencoded",
'sec-ch-ua':'"Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
"sec-ch-ua-mobile": "?0",
'sec-ch-ua-platform': '"Windows"',
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
"x-asbd-id": "198387",
"x-csrftoken": "RfrLPLyTlkMfwpamAJ0ORu3F4GufRMzP",
"x-ig-app-id": "936619743392459",
"x-ig-www-claim": "0",
"x-instagram-ajax": "bc3569920aaf",
"x-requested-with": "XMLHttpRequest"}
  data= {
"username": str(username),
"enc_password": "#PWD_INSTAGRAM_BROWSER:0:9775445428:"+str(password),
"optIntoOneTap": "false",
"queryParams": {},
"stopDeletionNonce": "",
"trustedDeviceRecords": {}}
  req = requests.post(url,headers=headers,data=data)
  print(req.text)
  if '"authenticated":true' in req.text:
   sessionid=req.cookies['sessionid']
   bot.reply_to(message,text=f"""
*✅ sessionid
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
ᯓ sessionid :*{sessionid}
*⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
 ✅ Account Isntagram
⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯*
*ᯓ User : *{username}
*ᯓ Pass : *{password}
*ᯓ Pass : *{username}:{password}
*⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯ ⌯
ᯓDv : @CC22Y
ᯓBy : @CC22M*""",parse_mode='markdown')
   print(sessionid)
  elif '"message":"checkpoint_required"' in req.text:
   bot.reply_to(message,text='🔐 secure Account') 
  elif '"authenticated":false' in req.text:
   u=("❌ Erorr Account ")
   print(u)
   bot.reply_to(message,text=u)
  else:
   u=("محظور شغل vpn")
   print(u)
   bot.reply_to(message,text=u)    
 except:
  bot.reply_to(message,text="عذرا لم اجد كهاذا زر!!")
   
bot.polling()
