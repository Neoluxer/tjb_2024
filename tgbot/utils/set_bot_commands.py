from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("add_lid", "Ввести заявку"),
        types.BotCommand("add_profit", "Внести доход"),
        types.BotCommand("cancel", "Сброс"),
        types.BotCommand("invoice", "Создать счет и акт"),
        types.BotCommand("worksheet_link", "Ссылка на анкету"),
        types.BotCommand("offer", "Ссылка на КП"),
        types.BotCommand("make_legal_contract", "Сделать договор с юр.лицом"),
        types.BotCommand("price", "Рассчитать стоимость"),
        types.BotCommand("make_contract","Создать договор с физ.лицом"),
        types.BotCommand("make_measuring_contract","Создать договор на обмеры"),
        types.BotCommand("profit_counter","подсчет прибыли за период"),


    ])
