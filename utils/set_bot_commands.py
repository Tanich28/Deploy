from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("test", "Тестирование"),
        types.BotCommand("menu", "Меню"),
        types.BotCommand("items", "Меню2"),
        types.BotCommand("parse_mode_html", "Парс"),
        types.BotCommand("get_cat", "Прислать кота"),
        types.BotCommand("more_cats", "Прислать больше котов"),
        types.BotCommand('set_photo', 'Установить фото в чате'),
        types.BotCommand('set_title', 'Установить название группы'),
        types.BotCommand('set_description', 'Установить описание группы'),
        types.BotCommand('ro', 'Режим Read only'),
        types.BotCommand('unro', 'Отключить RO'),
        types.BotCommand('ban', 'Забанить'),
        types.BotCommand('unban', 'Разбанить'),
        types.BotCommand('show_on_map', 'Показать на карте'),
        types.BotCommand('callback', 'контакт'),
        types.BotCommand('channels', 'Список каналов на подписку'),
        types.BotCommand('create_post', 'Предложить пост в канале'),
    ])





