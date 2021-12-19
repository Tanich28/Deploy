from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(resize_keyboard=True,
                            keyboard=[
                                [
                                     KeyboardButton(text="Котлетки")
                                ],
                                [
                                     KeyboardButton(text="Макарошки"),
                                     KeyboardButton(text="Пюрешка")
                                ]
                            ]
                           )