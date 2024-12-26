# main.py
from aiogram import executor
from confik import bot, dp, Admins
import logging
from handlers import commands, echo, quiz, fsm_reg ,fsm_store, send_products,delete_product,edit_product,send_one_products
import buttons
from db import main_db

async def on_startup(_):
    for admin in Admins:
        await  bot.send_message(chat_id=admin, text='Бот включен',
                                reply_markup=buttons.start_markup)
    await main_db.DataBase_creatr()


async def on_shutdown(_):
    for admin in Admins:
        await  bot.send_message(chat_id=admin, text='Бот выключен')


commands.register_commands_handlers(dp)
quiz.register_quiz_handlers(dp)
fsm_reg.register_fsmreg_handlers(dp)
fsm_store.register_fsmstore_handlers(dp)

send_products.register_handlers(dp)
delete_product.register_handlers(dp)
edit_product.register_handlers(dp)
send_one_products.register_handlers(dp)



echo.register_echo_handlers(dp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup,
                           on_shutdown=on_shutdown)
