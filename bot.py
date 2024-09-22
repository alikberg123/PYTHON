from config import Token
import telebot

bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
bot.infinity_polling()