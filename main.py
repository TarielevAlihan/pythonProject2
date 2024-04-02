import random
from random import choice
import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart
from dotenv import load_dotenv
from os import getenv
import logging

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()

@dp.message(Command('start'))
async def start_cmd(message: types.Message):
    await message.answer('Привет')

@dp.message(Command('info'))
async def info_cmd(message: types.Message):
    await message.answer(f"ваш никнейм: {message.from_user.username}\n"
                         f"ваш Id: {message.from_user.id}")

@dp.message(Command('picture'))
async def send_picture(message: types.Message):
    photos = ['forest.jpeg', 'images.jpeg']
    file = types.FSInputFile(f'images/{choice(photos)}')
    await message.answer_photo(photo=file, caption='ЛЕс')

@dp.message()
async def echo(message: types.Message):
    logging.info(message.text)
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())