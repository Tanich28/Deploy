from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile, Message, ContentType, MediaGroup

from loader import dp, bot


@dp.message_handler(content_types=ContentType.PHOTO)
async def get_file_id_p(message: Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=ContentType.VIDEO)
async def get_file_id_v(message: Message):
    await message.reply(message.video.file_id)


@dp.message_handler(Command("get_cat"))
async def send_cat(message: Message):
    photo_file_id = "AgACAgIAAxkBAAID0mEIUNw43drmqXdD_glTG48aHGAwAAKaszEbkIZISDJUEFrldLvXAQADAgADeQADIAQ"
    # photo = "https://www.meme-arsenal.com/memes/3f5777727d3f6e263b4edbee5bd15a1b.jpg" # URL
    # photo = InputFile(path_or_bytesio="photos/cat.jpg")  # Local file
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo_file_id,
                         caption="Вот тебе фото кота /more_cats")


@dp.message_handler(Command("more_cats"))
async def more_cats(message: Message):
    # Создаем альбом
    album = MediaGroup()

    # Прикрепляем фото и видео
    photo_file_id = "AgACAgIAAxkBAAID6mEJo2EqMWIszgFu1HnXtJcE7NnGAAKWtDEbkIZQSEoaaULH8-DpAQADAgADeQADIAQ"
    # photo_url = "https://https://yandex.ru/images/search?utm_source=main_stripe_big&text=%D0%9D%D1%"
    photo_bytes = InputFile("photos/cat.jpg")
    # video_file_id = "BQACAgIAAxkBAAID_mEJpb4rpgZIMsq__KGAc-QrRukFAAKdEQACkIZQSLw9bcxv6yhcIAQ"
    album.attach_photo(
        photo=photo_file_id,
        caption="Прикольный котик")
    # album.attach_photo(photo=photo_url)
    album.attach_photo(photo=photo_bytes)
    # album.attach_video(video=video_file_id,
    #                    caption="Видео где котик запрыгивает на кровать")

    # Отправляем
    # await bot.send_media_group(chat_id=message.from_user.id, media=album)
    await message.answer_media_group(media=album)
