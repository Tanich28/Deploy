from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
         KeyboardButton(text="contact",
                        request_contact=True)
        ]
    ],
    resize_keyboard=True
)
