from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from utils.db_api.user import User
#from aiogram.types import User


class GetBUser(BaseMiddleware):
    async def on_process_message(self, message:types.Message, data: dict):
        data['user'] = User(id=message.from_user.id, name=message.from_user.full_name)

    async def on_process_calback_query(self,cq: types.CallbackQuery, data:dict):
        data['user'] = User(id=666, name=cq.message.from_user.full_name)