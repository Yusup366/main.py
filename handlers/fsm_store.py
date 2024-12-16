# fsm_reg.py
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from buttons import cancel_markup, start_markup, yes_markup
from aiogram.types import ReplyKeyboardRemove
from db import main_db



class FSMStore(StatesGroup):
    Modelname = State()
    Size = State()
    Category = State()
    Price = State()
    Productid = State()
    Infoproduct = State()
    Photo = State()
    Submit = State()





async def start_fsm_story(message: types.Message):
    await message.answer('Название модели', reply_markup=cancel_markup)
    await FSMStore.Modelname.set()

async def load_modelname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['modelname'] = message.text

    await FSMStore.next()
    await message.answer('Укажите свой размер: ')


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await FSMStore.next()
    await message.answer('Укажите Категорию: ')


async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await FSMStore.next()
    await message.answer('Стоймоть: ')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await FSMStore.next()
    await message.answer('Отправте артикул: ')

async def load_productid(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['productid'] = message.text

    await FSMStore.next()
    await message.answer('Введите инфармацию продукта: ')

async def load_infoproduct(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['infoproduct'] = message.text

    await FSMStore.next()
    await message.answer('Отправте фотку продукта')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await FSMStore.next()
    await message.answer(f'Верные ли данные?',reply_markup=yes_markup)
    await message.answer_photo(photo=data['photo'],
                               caption=f'Название модели - {data["modelname"]}\n'
                             f'Размер - {data["size"]}\n'
                             f'Категория - {data["category"]}\n'
                             f'Стоимость - {data["price"]}\n'
                             f"Артикул - {data['productid']}\n"
                             f"Информация о продукте - {data['infoproduct']}",)


async def load_submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'Да'.lower():
        async with state.proxy() as data:
            await main_db.sql_insert_store(
                modelname=data['modelname'],
                Size=data['size'],
                Price=data['price'],
                Photo=data['photo'],
            )
            await main_db.sql_insert_product(
                productid=data['productid'],
                category=data['category'],
                infoproduct=data['infoproduct']
            )
            await message.answer('Ваши данные в базе!')
            await state.finish()

    elif message.text.lower() == 'Нет'.lower():
        await message.answer('Хорошо, отменено!')
        await state.finish()

    else:
        await message.answer('Введите Да или Нет!')

async def cancel_fsm(message: types.Message, state: FSMContext):
    curses_state = await state.get_state()

    #kb = ReplyKeyboardMarkup()

    if curses_state is not None:
        await state.finish()
        await message.answer('Отменено!',reply_markup=start_markup)


def register_fsmstore_handlers(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='Отмена',
                                                 ignore_case=True))

    dp.register_message_handler(start_fsm_story, commands=['store'])
    dp.register_message_handler(load_modelname, state=FSMStore.Modelname)
    dp.register_message_handler(load_size, state=FSMStore.Size)
    dp.register_message_handler(load_category, state=FSMStore.Category)
    dp.register_message_handler(load_price, state=FSMStore.Price)
    dp.register_message_handler(load_productid, state=FSMStore.Productid)
    dp.register_message_handler(load_infoproduct, state=FSMStore.Infoproduct)
    dp.register_message_handler(load_photo, state=FSMStore.Photo, content_types=['photo'])
    dp.register_message_handler(load_submit, state=FSMStore.Submit)
