import aiogram
import asyncio

# бот, доставщик, выполнитель
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN

# создаём поток для асинхронного приложения
# не нужен, так как он создаётся в диспатчере
# loop = asyncio.get_event_loop()

# создаём класс бота
bot = Bot(BOT_TOKEN, parse_mode="HTML")

# Создаём доставщик
dp = Dispatcher(bot)


if __name__ == "__main__":
    from handlers import dp, send_to_admin

    # запрос к телеграму через апдейтс, запоминает оффсет
    executor.start_polling(dp, on_startup=send_to_admin)


# import requests
#
# API_link = """https://api.telegram.org/bot1565175331:AAG2wfXyPKDG9_9MNIBsm8m7cqTn23SdEkA/"""
#
# updates = requests.get( API_link + "getUpdates?offset=-1").json()
#
# print(updates)
#
# # 0 - первый элемент массива
# message = updates["result"][0]["message"]
#
# chat_id = message["from"]["id"]
# text = message["text"]
#
# sent_message = requests.get(API_link + f"sendMessage?chat_id={chat_id}&text=You sent me {text}")