from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
         KeyboardButton(text="search",
                        request_location=True)
        ]
    ],
    resize_keyboard=True
)
