import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Настройка логов, чтобы видеть ошибки в панели Render
logging.basicConfig(level=logging.INFO)

TOKEN = "7292211910:AAHjL2K6mHqQy_39u_V8z6rI8lF7F1r8zZ8"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("✅ Бот запущен на Render!\nНапиши /monday или /tuesday")

@dp.message(Command("monday"))
async def monday(message: types.Message):
    await message.answer("📅 Понедельник:\n1. Математика\n2. Русский\n3. Английский")

@dp.message(Command("tuesday"))
async def tuesday(message: types.Message):
    await message.answer("📅 Вторник:\n1. Физика\n2. Химия\n3. Биология")

async def main():
    logging.info("Бот выходит в онлайн...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
