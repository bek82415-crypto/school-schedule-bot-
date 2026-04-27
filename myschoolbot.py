import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Настройка логов, чтобы видеть работу бота в панели Render
logging.basicConfig(level=logging.INFO)

# Твой новый рабочий токен
TOKEN = "8680343546:AAF3tUFCdLemv7rGCoqfUyQixdQtelZ1fU8"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("✅ Бот успешно запущен и готов к работе!\nНапиши /monday или /tuesday")

# Расписание на понедельник
@dp.message(Command("monday"))
async def monday_handler(message: types.Message):
    await message.answer("📅 Понедельник:\n1. Математика\n2. Русский язык\n3. Английский")

# Расписание на вторник
@dp.message(Command("tuesday"))
async def tuesday_handler(message: types.Message):
    await message.answer("📅 Вторник:\n1. Физика\n2. Химия\n3. Биология")

# Главная функция запуска
async def main():
    logging.info("Бот выходит в онлайн...")
    await dp.start_polling(bot)

# Правильный запуск (с двойными подчеркиваниями!)
if __name__ == "__main__":
    asyncio.run(main())
