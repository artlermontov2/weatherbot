import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

from api import get_weather

load_dotenv()

TOKEN = getenv("BOT_TOKEN")
API_KEY = getenv("API_KEY")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    text = (
        f"Привет, {html.bold(message.from_user.full_name)} 👋\n"
        f"Я бот для информации о погоде в твоём городе.\n"
        f"В тексте сообщения напиши название товего города👇"
    )
    await message.answer(text)


@dp.message()
async def get_city_weather(message: Message) -> None:
    try:
        msg = get_weather(message.text, API_KEY)

        await message.answer(msg)
    except KeyError:
        await message.answer("Не могу найти такой город")



async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())