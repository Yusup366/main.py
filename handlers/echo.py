from aiogram import types,Dispatcher
from confik import bot
import random

from pyexpat.errors import messages

async def game(message: types.Message):
    dice_random = random.choice(['⚽', '🎰', '🏀', '🎯', '🎳', '🎲'])
    await bot.send_dice(chat_id=message.from_user.id, emoji=dice_random)


async def echo_handler(message: types.Message):
    try:
        num = float(message.text)
        square = num ** 2
        await  message.answer(f'Квадрат числа {num} равен {square}')
    except ValueError:
        await message.answer(message.text)



def register_echo_handlers(dp: Dispatcher):
    dp.register_message_handler(game, commands=['game'])
    dp.register_message_handler(echo_handler, lambda message: not message.text.startswith('/'))
