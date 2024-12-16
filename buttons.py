from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton



cancel_markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
cancel_button = KeyboardButton('Отмена')
cancel_markup.add(cancel_button)

start_markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
start_markup.add(KeyboardButton('/start'),KeyboardButton('/store'),
                 KeyboardButton('/quiz'),KeyboardButton('/registration'),
                 KeyboardButton('/game'))

yes_markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
yes_markup.add(KeyboardButton("Да"), KeyboardButton("Нет"))