# -*- coding: utf-8 -*-
from aiogram import Dispatcher
from aiogram import types


async def offer(message: types.Message):
    await message.answer('<a href="192.168.31.150:8000/offer">192.168.31.150:8000/offer</a>',parse_mode="HTML")


def register_add_offer(dp: Dispatcher):
    dp.register_message_handler(offer, commands=["offer"], state="*")
