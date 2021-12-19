from aiogram import types
from loader import dp,bot

@dp.message_handler()
async def message (m: types.Message):
    #await bot.delete_message(m.chat.id, m.message_id)
    await m.delete