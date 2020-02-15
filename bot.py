#!/usr/bin/python
# -*- coding: utf8 -*-
import logging
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

import aiohttp

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
PROXY_URL = os.getenv("TELEGRAM_PROXY_URL")

PROXY_AUTH = aiohttp.BasicAuth(
    login=os.getenv("TELEGRAM_PROXY_LOGIN"),
    password=os.getenv("TELEGRAM_PROXY_PASSWORD")
)

bot = Bot(token=API_TOKEN, proxy=PROXY_URL, proxy_auth=PROXY_AUTH)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
     This handler will be called when user sends `/start` or `/help` command
     """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
