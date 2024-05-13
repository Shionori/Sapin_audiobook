from telebot import TeleBot
from telebot import types


bot = TeleBot('7003086115:AAFDKNRuuiwqgwoYAK3vzwhil-zpvIGSPSI') #Токен бота

@bot.message_handler(content_types=['text'])
def handler(message):
    if message.text != "":
        bot.send_message(message.chat.id, 'Бот находится на техническом обслуживании.\n\nПопробуйте повторить попытку позже.')
bot.polling(none_stop=True)