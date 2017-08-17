from telebot import types

import config
import telebot

bot = telebot.TeleBot(config.token)
markup = types.ReplyKeyboardMarkup()
markupRem = types.ReplyKeyboardRemove(selective=False)
markupF = types.ForceReply(selective=False)


#
# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
#     bot.send_message(message.chat.id, message.text)


@bot.message_handler(commands=['vk'])
def handle_start_help(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Сайт факультета", url="vk.com/mmf_dnu")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Сайт механико-математического факультета", reply_markup=keyboard)
    # bot.send_message(message.chat.id, "www.vk.com/mmf_dnu")


@bot.message_handler(commands=['fb'])
def handle_start_help(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Сайт факультета", url="http://mmf.dnepredu.com")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Сайт механико-математического факультета", reply_markup=keyboard)
    bot.send_message(message.chat.id, "www.facebook.com/groups/mmf.dnu")


@bot.message_handler(commands=['inst'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "https://www.instagram.com/mmf_dnu")


@bot.message_handler(commands=['site'])
def handle_start_help(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Сайт факультета", url="http://mmf.dnepredu.com")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Сайт механико-математического факультета", reply_markup=keyboard)
    #
    # bot.send_message(message.chat.id, "www.facebook.com/groups/mmf.dnu")



@bot.message_handler(commands=['integral'])
def handle_start_help(message):
    photo = open('integral.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    # quick answer
    bot.send_message(message.chat.id, "Таблица интегралов", reply_markup=markupF)
    # bot.send_message(message.chat.id, "www.facebook.com/groups/mmf.dnu")


@bot.message_handler(content_types=["text"])
def default_test(message):
    if message.text == "Сайт":
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Сайт ММФ ДНУ", url="http://mmf.dnepredu.com/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Открыть сайт факультета", reply_markup=keyboard)
    if message.text == "Дай стипуху":
        markup.row('Ага', 'Щас')
        markup.row('Бегу', 'Несу', 'На')
        bot.send_message(message.chat.id, "Выбирай", reply_markup=markup)
        bot.send_message(message.chat.id, "", reply_markup=markupRem)
    else:
        bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
