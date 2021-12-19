import logging

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_button import choice, pear_keyboard
from loader import dp



@dp.message_handler(Command('items'))
async def show_items(message: types.Message):
    await message.answer(text='На продажу у нас есть 2 товара: 5 Яблок и 1 груша. \n'
                             'Если вам ничего не нужно - жмите отмену',

                         reply_markup=choice)

@dp.callback_query_handler(buy_callback.filter(item_name='pear'))
async def buying_pear(call: CallbackQuery, callback_data: dict):
    #await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer(cache_time=60)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict= {callback_data}')
    quantatity = callback_data.get('quantity')
    await call.message.answer(f'Вы выбрали купить грушу. Груш всего {quantatity}. Спасибо.',
                              reply_markup=pear_keyboard)

@dp.callback_query_handler(text='cancel')
async def cancel(call: CallbackQuery):
    await call.answer('Вы отменили покупку', show_alert=True)
    await call.message.edit_reply_markup()