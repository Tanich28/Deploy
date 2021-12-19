import os

from flask import Flask

from data.config import APP_URL
from loader import bot
from utils.set_bot_commands import set_default_commands

server = Flask(__name__)
async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    await bot.set_webhook(APP_URL)
    await on_startup_notify(dp)
    await set_default_commands(dp)


# if __name__ == '__main__':
#     from aiogram import executor
#     from handlers import dp
#
#     executor.start_polling(dp, on_startup=on_startup)


if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
