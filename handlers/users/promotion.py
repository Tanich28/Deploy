from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

# from data.config import channels
from data.config import channels
from filters.forwarded_message import IsForwarded
# from handlers import channels
from keyboards.inline.subscription import check_button
from loader import dp, bot
# from utils.misc import subscription
from utils.misc import subscription


@dp.message_handler(IsForwarded(), content_types=types.ContentType.ANY)
async def get_channel_info(message: types.Message):
    await message.answer(f'Сообщение прслано из канала {message.forward_from_chat.title}.\n'
                         f'Username:@{message.forward_from_chat.username}\n'
                         f'ID: {message.forward_from_chat.id}')


@dp.message_handler(Command("channels"))
async def show_channels(message: types.Message):
    channels_format = str()
    for channel in channels:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        channels_format += f"Канал {invite_link}\n"
    await message.answer(f"Вам необходимо подписаться на следующие каналы: \n"
                         f"{channels_format}",
                         reply_markup=check_button,
                         disable_web_page_preview=True
                         )


@dp.callback_query_handler(text="check_subs")
async def checker(call: CallbackQuery):
    await call.answer()
    result = str()
    for channel in channels:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f'Подписка на канал <b>{channel.title}</b> Оформлена!\n\n'
        else:
            invite_link = await channel.export_invite_link()
            result += (f'Подписка на канал <b>{channel.title}</b> не оформлена!'
                       f"<a href='{invite_link}'>Нужно подписаться.</a.\n\n")
    await call.message.answer(result, disable_web_page_preview=True
                              )
