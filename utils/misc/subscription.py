from typing import Union
from aiogram import Bot

from loader import bot
# from aiogram import Bot


async def check(user_id, channel: Union[int, str]):
    # bot = Bot.get_current
    member = await Bot.get_chat_member(chat_id=channel, user_id=user_id, self=bot)
    return member.is_chat_member()
