# -*- coding: utf-8 -*-
from aiogram import Dispatcher
from aiogram import types


async def bot_start(message: types.Message):
    await message.answer('<a href="https://forms.gle/baXFEog1vcuKDRrq5">Ссылка на анкету</a>',parse_mode="HTML")


def register_add_link(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=["worksheet_link"], state="*")
