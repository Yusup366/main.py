from aiogram import types, Dispatcher
import os
from confik import bot
from handlers.echo import game



async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Hello {message.from_user.first_name}!\n'
                                f'Твой Telegram ID - {message.from_user.id}')

async def mem_handler(message: types.Message):
    photo_path = os.path.join('media','img.png')
    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo=photo, caption='Мемчик')




def register_commands_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(mem_handler, commands=['mem'])
    dp.register_message_handler(game, commands=['game'])
