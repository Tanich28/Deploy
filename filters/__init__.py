from aiogram import Dispatcher
from .admins import AdminFilter
from .group_chat import IsGroup
from .forwarded_message import IsForwarded

from .private_chat import IsPrivate
# from .is_admin import AdminFilter


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsForwarded)

#Нужно прописывать подвязку всех созданных фильтров
