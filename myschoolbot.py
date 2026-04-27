import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Твой токен (проверь, чтобы не было лишних пробелов)
TOKEN = "7292211910:AAHjL2K6mHqQy_39u_V8z6rI8lF7F1r8zZ8"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет! Я твой бот с расписанием.\nНапиши /monday или /tuesday")

# Команда /monday
@dp.message(Command("monday"))
async def monday_handler(message: types.Message):
    schedule = (
        "📅 Понедельник:\n"
        "1. Математика\n"
        "2. Русский язык\n"
        "3. Английский язык"
    )
    await message.answer(schedule)

# Команда /tuesday
@dp.message(Command("tuesday"))
async def tuesday_handler(message: types.Message):
    schedule = (
        "📅 Вторник:\n"
        "1. Физика\n"
        "2. Химия\n"
        "3. Биология"
    )
    await message.answer(schedule)

# Главная функция запуска
async def main():
    print("✅ Бот успешно запущен и готов к работе!")
    await dp.start_polling(bot)

# Самая важная строчка (проверь подчеркивания!)
if __name__ == "__main__":
    asyncio.run(main())
