import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Твой токен
TOKEN = "8713248266:AAHl5og8s5hXYvEoFwuUWOX6ooZyYOBbXe0"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="Понедельник"), types.KeyboardButton(text="Вторник"))
    builder.row(types.KeyboardButton(text="Среда"), types.KeyboardButton(text="Четверг"), types.KeyboardButton(text="Пятница"))
    return builder.as_markup(resize_keyboard=True)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я твой бот с расписанием. Выбери день недели:", reply_markup=get_keyboard())

@dp.message(F.text.in_({"Понедельник", "Вторник", "Среда", "Четверг", "Пятница"}))
async def show_schedule(message: types.Message):
    days = {
        "Понедельник": "📅 ПН: 09:30-10:50 Колледж",
        "Вторник": "📅 ВТ: 08:00-12:20 Уроки",
        "Среда": "📅 СР: 08:00-13:50 Уроки",
        "Четверг": "📅 ЧТ: 08:00-13:50 Уроки",
        "Пятница": "📅 ПТ: 08:00-13:50 Уроки"
    }
    await message.answer(days[message.text])

async def main():
    print("✅ Бот запущен на Render!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
