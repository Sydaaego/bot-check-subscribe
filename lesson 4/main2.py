import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

logging.basicConfig(level=logging.INFO)
bot = Bot(token="8780316227:AAHEZOBygVKrGwf88k5rDglVIV7EROB5yX4")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    button1 = types.InlineKeyboardButton(text = "Проверить подписку", callback_data = "follow_check")
    builder.row(button1)
    text = 'Добро пожаловать в bot!'
    await bot.send_photo(message.chat.id, photo = "https://avatars.mds.yandex.net/i?id=828206096ba74379c0c051dcfadd952f_l-4570132-images-thumbs&n=13", caption = text, reply_markup = builder.as_markup(), parse_mode = "HTML")

@dp.callback_query(F.data == "follow_check")
async def cmd_follow(callback: types.CallbackQuery):
    await callback.answer()
    user_channel_status = await bot.get_chat_member(chat_id = '@your_channel', user_id = callback.from_user.id) 
    if user_channel_status.status != 'left':
        text = 'Да, теперь ты подписан на @your_channel'
        await callback.message.answer(text, parse_mode = 'HTML')
    else:
        text = 'Ты все еще не подписан на @your_channel. Для продолжения надо подписаться 👀'
        await callback.message.answer(text, parse_mode = 'HTML')

async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())






