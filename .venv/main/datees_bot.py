import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

bot = Bot(token='7923155027:AAG8zvHmsuFDT0y1xakOtYtPPDCLok3ypJE')
dp = Dispatcher()


@dp.message(CommandStart())
async def echo(message: Message):
    await message.answer('здравствуй странник! Как тебя зовут? Представься')


@dp.message(F.text == 'Влад')
async def balance(message: Message):
    await message.answer('Слава Игилу!')


@dp.message(F.text == 'Владислав')
async def balance(message: Message):
    await message.answer('Слава России!')


@dp.message(F.text == 'Долбаеб')
async def balance(message: Message):
     await message.answer('дед твой долбаеб, дура')


@dp.message(F.text == 'Илья')
async def balance(message: Message):
    await message.answer('Лапука лох')



@dp.message(F.text == 'Как дела?')
async def nice(message: Message):
    await message.answer('это тебя ебать не должно')


@dp.message(F.text == 'Эмилия')
async def balance(message: Message):
    await message.answer('Сделай Вадиму покушац')


@dp.message(F.text == 'Нет')
async def balance(message: Message):
    await message.answer('пидора ответ')


@dp.message(F.text == 'Вадим')
async def balance(message: Message):
    await message.answer('*Низкий поклон королю*')


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
