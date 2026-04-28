import telebot
from telebot import types

# Твой токен
bot = telebot.TeleBot('8680343546:AAF3tUFCdLemv7rGCoq_oM1p_u19qYp7Y0w')

# Твое новое расписание
schedule = {
    "Понедельник": "1. 🇰🇬 Кыргызский язык (09:30-10:50)\n2. 🧬 Биология (11:00-12:20)\n3. 🪖 НВП (12:30-13:50)",
    "Вторник": "1. 📚 Мировая литература (08:00-09:20)\n2. 🧪 Химия (09:30-10:50)\n3. ⚽️ Физкультура (11:00-12:20)",
    "Среда": "1. 🇰🇬 История Кыргыстана (08:00-09:20)\n2. 🎓 Введение в спец. (09:30-10:50)\n3. 💻 Цифр. грамотность (11:00-12:20)\n4. 🍎 Физика (12:30-13:50)",
    "Четверг": "1. 🔢 Математика (08:00-09:20)\n2. 📖 Кырг. литература (09:30-10:50)\n3. 🇬🇧 Английский язык (11:00-12:20)\n4. 🔢 Математика (12:30-13:50)",
    "Пятница": "1. 🎓 Введение в спец. (08:00-09:20)\n2. 🔢 Математика (09:30-10:50)\n3. 🔭 Астрономия (11:00-12:20)\n4. 🗣 Культура речи (12:30-13:50)"
}

@bot.message_handler(commands=['start'])
def start(message):
    # Создаем кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Понедельник")
    btn2 = types.KeyboardButton("Вторник")
    btn3 = types.KeyboardButton("Среда")
    btn4 = types.KeyboardButton("Четверг")
    btn5 = types.KeyboardButton("Пятница")
    
    markup.add(btn1, btn2, btn3, btn4, btn5)
    
    bot.send_message(message.chat.id, "Привет! Выбери день недели, чтобы узнать расписание 👇", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    day = message.text.capitalize()
    if day in schedule:
        bot.send_message(message.chat.id, f"📅 *{day}*:\n\n{schedule[day]}", parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, "Нажми на одну из кнопок ниже 👇")

bot.polling(none_stop=True)
