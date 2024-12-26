from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyexpat.errors import messages

from confik import bot


async def quiz_1(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)

    button = InlineKeyboardButton('Далее', callback_data='quiz_2')
    keyboard.add(button)

    question = 'XBOX or Sony'
    answer = ['XBOX','Sony','Nintendo']

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='Жаль...',
        open_period=60,
        reply_markup=keyboard

    )

async def quiz_2(call: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)

    button = InlineKeyboardButton('Далее', callback_data='quiz_3')
    keyboard.add(button)

    question = 'Python, JavaScript, Java, PHP and Swift'
    answer = ['Python','JavaScript','PHP','Swift']


    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation='Все с тобой понятно',
        open_period=180,
        reply_markup=keyboard

    )

async def quiz_3(callback: types.CallbackQuery):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True, row_width=1)

    question = 'Футбол','Батскетбол','Тенис'
    answer = ['Футбол','Батскетбол','Тенис']

    await bot.send_poll(
        chat_id=callback.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='Футбол топ!',
        open_period=60,

    )

def register_quiz_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands='quiz')
    dp.register_callback_query_handler(quiz_2, text='quiz_2')
    dp.register_callback_query_handler(quiz_3, text='quiz_3')