from main import bot, dp
from aiogram.types import Message
from config import ADMIN_ID


async def send_to_admin(*args):
    await bot.send_message(chat_id=ADMIN_ID, text="Бот запущен")


@dp.message_handler()
async def echo(message: Message):
    text = f"Hello, you are wrote {message.text}"
    await bot.send_message(chat_id=message.from_user.id, text=text)
    # Либо так, функция библиотеки, которая забирает айди юзера
    await message.answer(text=text)
