from main import bot, dp

from  aiogram.types import Message
from  config import admin_id

async  def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text= "Бот Обнови Обои запущен")

@dp.message_handler()
async def echo(message: Message):
    text = f"Привет, я еще не готов ! но я уже понимаю что ты написал мне : {message.text}"
    await message.answer(text=text)

