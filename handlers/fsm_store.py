# fsm_reg.py
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from buttons import cancel_markup, start_markup
from aiogram.types import ReplyKeyboardRemove


class FSMStore(StatesGroup):
    modelname = State()
    Size = State()
    Category = State()
    Price = State()
    Photo = State()
    Submit = State()


async def start_fsm_story(message: types.Message):
    await message.answer('Название модели', reply_markup=cancel_markup)
    await FSMStore.modelname.set()

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
    await message.answer('Отправьте  фотку товара: ')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await FSMStore.next()
    await message.answer(f'Верные ли данные?')
    await message.answer_photo(photo=data['photo'],
                               caption=f'Название модели - {data["modelname"]}\n'
                             f'Размер - {data["size"]}\n'
                             f'Категория - {data["category"]}\n'
                             f'Стоимость - {data["price"]}\n')


async def load_submit(message: types.Message, state: FSMContext):
    if message.text == 'Да':
        async with state.proxy() as data:
            # Запись в базу
            await message.answer('Ваши данные в базе!')
            await state.finish()

    elif message.text == 'Нет':
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
    dp.register_message_handler(load_modelname, state=FSMStore.modelname)
    dp.register_message_handler(load_size, state=FSMStore.Size)
    dp.register_message_handler(load_category, state=FSMStore.Category)
    dp.register_message_handler(load_price, state=FSMStore.Price)
    dp.register_message_handler(load_photo, state=FSMStore.Photo, content_types=['photo'])
    dp.register_message_handler(load_submit, state=FSMStore.Submit)
