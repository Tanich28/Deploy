from loader import dp

@dp.message_handler()
async def e(m):
    await m.answer(m.text)