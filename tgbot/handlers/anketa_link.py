# -*- coding: utf-8 -*-
from aiogram import Dispatcher
from aiogram import types


async def bot_start(message: types.Message):
    await message.answer("https://forms.gle/H6fJyodn7qU5qVyD8")


def register_add_link(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=["worksheet_link"], state="*")
