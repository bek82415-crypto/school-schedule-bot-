import telebot
from telebot import types

# Твой токен подставил сам
bot = telebot.TeleBot('8680343546:AAF3tUFCdLemv7rGCoq_oM1p_u19qYp7Y0w')

# ТУТ ПРОСТО ЗАМЕНИ ТЕКСТ НА СВОИ УРОКИ
schedule = {
    "Понедельник": "1. Математика\n2. Русский язык\n3. История",
    "Вторник": "1. Физика\n2. Химия\n3. Биология",
    "Среда": "1. Английский\n2. Физкультура",
    "Четверг": "1. География\n2. Литература",
    "Пятница": "1. Информатика\n2. Обществознание"
}

@bot.message_handler(commands=['start'])
def start(message):
    # Создаем удобные кнопки внизу
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Понедельник")
    btn2 = types.KeyboardButton("Вторник")
    btn3 = types.KeyboardButton("Среда")
    btn4 = types.KeyboardButton("Четверг")
    btn5 = types.KeyboardButton("Пятница")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    
    bot.send_message(message.chat.id, "Привет! Выбери день недели на кнопках ниже 👇", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_schedule(message):
    day = message.text
    if day in schedule:
        bot.send_message(message.chat.id, f"📅 *{day}*:\n{schedule[day]}", parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, "Пожалуйста, нажми на кнопку с днем недели!")

bot.polling(none_stop=True)
