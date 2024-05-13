from telebot import TeleBot
from keyboards import *


bot = TeleBot('7003086115:AAFDKNRuuiwqgwoYAK3vzwhil-zpvIGSPSI') #Токен бота
number = '79851969099'


@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id < 0:
        return print(message.chat.id)
    if not message.chat.username:
        bot.send_message(message.chat.id, "Для пользования ботом установите username в настройках телеграмма.")
    else:
        global markup
        markup = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton("Остеология", callback_data="Ost")
        b2 = types.InlineKeyboardButton("Артросиндесмология", callback_data="Art")
        markup.row(b1,b2,)
        b3 = types.InlineKeyboardButton("Пищеварительная система", callback_data='Pish')
        b4 = types.InlineKeyboardButton("Дыхательная система", callback_data='Duh')
        markup.row(b3, b4)
        b5 = types.InlineKeyboardButton("Мочеполовой аппарат", callback_data='Mocha')
        b6 = types.InlineKeyboardButton("Органы кроветворения и иммунной защиты", callback_data='Bleed')
        markup.row(b5, b6)
        b7 = types.InlineKeyboardButton("Эндокринные железы", callback_data='Endo')
        b8 = types.InlineKeyboardButton("Ангиология", callback_data='Ang')
        markup.row(b7, b8)
        b9 = types.InlineKeyboardButton("ЦНС", callback_data='CNS')
        b10 = types.InlineKeyboardButton("ПНС", callback_data="PNS")
        markup.row(b9, b10)
        b11 = types.InlineKeyboardButton("ВНС", callback_data='VNS')
        b12 = types.InlineKeyboardButton("Эстезиология", callback_data='Estez')
        b13 = types.InlineKeyboardButton("Миология", callback_data='Mio')
        markup.row(b11, b12, b13)
        bot.reply_to(message, "<em>Дорогой коллега, этот бот был разработан для облегчения твоего обучения.\n"
                                    "Желаем тебе удачи!\n"
                                    "(Бот является студенческим проектом)</em>", reply_markup=markup, parse_mode='html')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Для перезапуска бота необходимо прописать /start')

@bot.message_handler(content_types=['text'])
def handler(message):
    if message.text == "ЦНС" or message.text == "Цнс":
        bot.send_message(message.chat.id, 'Выберите нужный пункт \n\n', reply_markup=CNS)

@bot.callback_query_handler(func=lambda call: True)
def yumikoGay(call):

    if call.data == "GM":
        bot.edit_message_text('<b> Выберите нужный пункт </b>', chat_id=call.message.chat.id,
                              message_id=call.message.message_id, reply_markup=P_GM, parse_mode='html')
    if call.data == "CNS":
        bot.edit_message_text('<b> Выберите нужный пункт </b>', chat_id=call.message.chat.id,
                              message_id=call.message.message_id, reply_markup=CNS, parse_mode='html')
    if call.data == "markup":
        bot.edit_message_text('<b> Выберите нужный пункт </b>', chat_id=call.message.chat.id,
                              message_id=call.message.message_id, reply_markup=markup, parse_mode='html')
    if call.data == "BM":
        bot.edit_message_text('<b> Выберите нужный пункт </b>', chat_id=call.message.chat.id,
                              message_id=call.message.message_id, reply_markup=P_BM, parse_mode='html')
    if call.data == "SB":
        bot.edit_message_text('<b> Выберите нужный пункт </b>', chat_id=call.message.chat.id,
                              message_id=call.message.message_id, reply_markup=P_SB, parse_mode='html')
    if call.data == "PM":
        bot.edit_message_text('<b> Выберите нужный пункт </b>', chat_id=call.message.chat.id,
                              message_id=call.message.message_id, reply_markup=P_PM, parse_mode='html')
    if call.data == "P_GM":
        bot.edit_message_text('<b> Выберите нужный пункт </b>', chat_id=call.message.chat.id,
                              message_id=call.message.message_id, reply_markup=P_GM, parse_mode='html')
    if call.data == "LB":
        bot.edit_message_text('<b> Выберите нужный пункт </b>', chat_id=call.message.chat.id,
                              message_id=call.message.message_id, reply_markup=P_LB, parse_mode='html')
    if call.data == "PrB":
        audio = open(r'audio/9. Промежуточный моз.mp3', 'rb')
        bot.send_audio(call.message.chat.id, audio),
    if call.data == "TZh":
        audio = open(r'audio/10_Третий_желудочек_Средний_мозг_Перешеек_ромбовидного_мозга.mp3','rb')
        bot.send_audio(call.message.chat.id , audio)
    if call.data == "AD":
        audio = open(r'audio/Общая информация.mp3', 'rb')
        bot.send_audio(call.message.chat.id, audio)
    if call.data == "GrBl":
        audio = open(r'audio/Серое белое вещество спинного мозга.mp3', 'rb')
        bot.send_audio(call.message.chat.id, audio)
    if call.data == "PrSt":
        audio = open(r'audio/проводящие пути спинного мозга.mp3', 'rb')
        bot.send_audio(call.message.chat.id, audio)
    if call.data == "ShBr":
        audio = open(r'audio/оболочки спинного мозга.mp3', 'rb')
        bot.send_audio(call.message.chat.id, audio)
    if call.data == "AGEVAR":
        audio = open(r'audio/5_Возрастные_особенности_головного_м_озга.mp3', 'rb')
        bot.send_audio(call.message.chat.id, audio)
    if call.data == "BB":
        audio = open(r'audio/11. Задний мозг.mp3', 'rb')
        bot.send_audio(call.message.chat.id, audio)
    if call.data == "SBr":
        audio = open(r'audio/1. Продолговатый мозг..mp3', 'rb')
        bot.send_audio(call.message.chat.id, audio)
    if call.data == "FZh":
        audio = open(r'audio/2. Четвертый желудочек.mp3', 'rb')
        bot.send_audio(call.message.chat.id, audio)
    if call.data == "Rmb":
        audio = open(r'audio/3. Ромбовидная ямка.mp3', 'rb')
        bot.send_audio(call.message.chat.id, audio)
    if call.data == "FTW":
        audio = open(r'audio/4. 5 пара-12 пара.mp3', 'rb')
        bot.send_audio(call.message.chat.id, audio)
    if call.data == "Bl":
        audio = open(r'audio/Кровеносные сосуды головного мозга.mp3', 'rb')
        bot.send_audio(call.message.chat.id, audio)
    if call.data == "ShMB":
        audio = open(r'audio/Оболочки головного мозга.mp3','rb')
        bot.send_audio(call.message.chat.id, audio)
    if call.data == "Sin":
        audio = open(r'audio/Синусы твердой оболочки г.м.mp3','rb')
        bot.send_audio(call.message.chat.id, audio)
    if call.data == "SNsh":
        audio = open(r'audio/Сосуды и нервы твердой оболочки.mp3','rb')
        bot.send_audio(call.message.chat.id, audio)


bot.polling(none_stop=True)



