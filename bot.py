import config
import logging
import telebot
import random
from telebot import types

bot = telebot.TeleBot(config.TOKEN)




@bot.message_handler(commands=['start'])
def wellcome(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Random number")
    item2 = types.KeyboardButton("How r u?")
    markup.add(item1 , item2)

    bot.send_message(message.chat.id , "Добро пожаловать ,{0.first_name}!\n Я - <b>{1.first_name}</b> , бот созданный чтобы тестировать написание код на питоне.".format(message.from_user, bot.get_me()),
                    parse_mode='html' , reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if(message.chat.type=='private'):
        if(message.text=="Random number"):
            bot.send_message(message.chat.id , str(random.randint(0 , 20)))
        elif message.text=="How r u?":
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Im ok" , callback_data='ok')
            item2 = types.InlineKeyboardButton("Not bad", callback_data='bad')
            markup.add(item1 , item2)
            bot.send_message(message.chat.id ,message.text , reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'What do u say i dont undestood you?')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data =='ok':
                bot.send_message(call.message.chat.id , 'Вот и отличненько')
            elif call.data =='bad':
                bot.send_message(call.message.chat.id , 'Бывает')
            #remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id , text="How r u?",
                                  reply_markup=None)
            #show alert
            bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=True,
                                      text="This is alers!!!")
    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)