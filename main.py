import telebot


token = '7367321933:AAFGQqo63iYZqTj7liHqLH6SLxPmIL8ig_w'
bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
