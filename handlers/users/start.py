from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from utils.db_api import User
from utils.misc import rate_limit


@rate_limit(limit=10)
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!\n ')
