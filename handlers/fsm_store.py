from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from buttons import cancel_markup, start_markup, yes_markup
from aiogram.types import ReplyKeyboardRemove
from db import main_db



class FSMStore(StatesGroup):
    name_product = State()
    Size = State()
    Category = State()
    Price = State()
    Product_id = State()
    Info_product = State()
    Collection = State()
    Photo = State()
    Submit = State()





async def start_fsm_story(message: types.Message):
    await message.answer('Название модели', reply_markup=cancel_markup)
    await FSMStore.name_product.set()

async def load_name_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_product'] = message.text

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

async def load_product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await FSMStore.next()
    await message.answer('Введите инфармацию продукта: ')

async def load_info_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['info_product'] = message.text

    await FSMStore.next()
    await message.answer('Название вашей колекций')

async def load_collection(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['collection'] = message.text

    await FSMStore.next()
    await message.answer('Добавте фото продукта!')

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await FSMStore.next()
    await message.answer(f'Верные ли данные?',reply_markup=yes_markup)
    await message.answer_photo(photo=data['photo'],
                               caption=f'Название модели - {data["name_product"]}\n'
                             f'Размер - {data["size"]}\n'
                             f'Категория - {data["category"]}\n'
                             f'Стоимость - {data["price"]}\n'
                             f"Артикул - {data['product_id']}\n"
                             f"Информация о продукте - {data['info_product']}\n"
                             f"Добавленно в вашу коллекцию - {data['collection']}")


async def load_submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'Да'.lower():
        async with state.proxy() as data:
            await main_db.sql_insert_store(
                name_product=data['name_product'],
                size=data['size'],
                price=data['price'],
                product_id=data['product_id'],
                photo=data['photo'],
            )
            await main_db.sql_insert_product(
                product_id=data['product_id'],
                category=data['category'],
                info_product=data['info_product']
            )
            await main_db.sql_insert_collection(
                collection=data['collection'],
                product_id=data['product_id']
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
    dp.register_message_handler(load_name_product, state=FSMStore.name_product)
    dp.register_message_handler(load_size, state=FSMStore.Size)
    dp.register_message_handler(load_category, state=FSMStore.Category)
    dp.register_message_handler(load_price, state=FSMStore.Price)
    dp.register_message_handler(load_product_id, state=FSMStore.Product_id)
    dp.register_message_handler(load_info_product, state=FSMStore.Info_product)
    dp.register_message_handler(load_collection, state=FSMStore.Collection)
    dp.register_message_handler(load_photo, state=FSMStore.Photo, content_types=['photo'])
    dp.register_message_handler(load_submit, state=FSMStore.Submit)