import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

bot = Bot(token='')
dp = Dispatcher()


@dp.message(CommandStart())
async def echo(message: Message):
    await message.answer('Hello')


async def main():
    await dp.start_polling(bot)


asyncio.run(main())