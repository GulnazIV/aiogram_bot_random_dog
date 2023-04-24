from loader import dp
from aiogram import types

from utils import dog


@dp.message_handler()
async def cmd_help(message: types.Message):
    if message.text == '1':
        await message.answer_photo(photo=dog.random_dog())
        return
    await message.answer(text='Enter 1')
