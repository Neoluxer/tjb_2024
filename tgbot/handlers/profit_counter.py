# -*- coding: utf-8 -*-
from datetime import datetime

from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from tgbot.keyboards.menu import years, months
from tgbot.misc.profit_states import Profit_filter
from tgbot.models.profit_filter import average_profit, get_difference_is_month, get_sum_all_prices
from tgbot.models.profit_filter import get_sum_is_year, get_sum_is_source, get_sum_is_customer_name, get_sum_is_month
from tgbot.models.profit_filter import percentage_of_income_for_period


async def profit_preview(message: types.Message):
    await message.answer("Введите год\n", reply_markup=years)

    await Profit_filter.first()


async def enter_year(message: types.Message, state: FSMContext):
    answer1 = message.text
    async with state.proxy() as data:
        data["answer"] = answer1
    await message.answer("Введите месяц: ", reply_markup=months)
    await Profit_filter.next()


async def enter_month(message: types.Message, state: FSMContext):
    answer2 = message.text  # Месяц
    async with state.proxy() as data:
        answer1 = data.get("answer")  # Год

    last_year = int(answer1) - 1
    curent_year = datetime.now()
    year_now = curent_year.year
    profit_current_month = await get_sum_is_month(year=answer1, month=answer2)
    profit_current_month_last_year = await get_sum_is_month(year=last_year, month=answer2)
    profit_5_year = await get_sum_is_year(year=year_now - 5)
    profit_4_year = await get_sum_is_year(year=year_now - 4)
    profit_3_year = await get_sum_is_year(year=year_now - 3)
    profit_2_year = await get_sum_is_year(year=year_now - 2)
    profit_1_year = await get_sum_is_year(year=year_now - 1)
    profit_0_year = await get_sum_is_year(year=year_now)
    profit_current_year = await get_sum_is_year(year=answer1)
    difference = await get_difference_is_month(year=last_year, month=answer2)
    avprofit = await average_profit()
    all_profit = await get_sum_all_prices()
    complectation_profit = await get_sum_is_source(1)
    project_profit1 = await get_sum_is_source(2)
    project_profit2 = await get_sum_is_source(3)
    project_profit3 = await get_sum_is_source(4)
    project_profit4 = await get_sum_is_source(5)
    project_profit_all = project_profit1 + project_profit2 + project_profit3 + project_profit4
    supervision_profit = await get_sum_is_source(6)
    measurements_profit = await get_sum_is_source(8)
    floor_plan_profit = await get_sum_is_source(10)
    fore_project_profit = await get_sum_is_source(9)
    zuber_profit = await get_sum_is_customer_name("Зубер Виталий Игоревич")
    telelinskiy_profit = await get_sum_is_customer_name("Телелинский Дмитрий")
    chadigov_profit = await get_sum_is_customer_name("Чедыгов Аслан")
    petuhova_profit = await get_sum_is_customer_name("Петухова Екатерина Сергеевна")
    nyagu_profit = await get_sum_is_customer_name("Нягу Сергей")
    trapezdnikov_profit = await get_sum_is_customer_name("Трапездников Вячеслав")
    zaur_profit = await get_sum_is_customer_name("Хубецов Заурбек")
    drozdov_profit = await get_sum_is_customer_name("Дроздов Константин")


    comlectation_profit = await percentage_of_income_for_period(year=answer1, month=answer2, category=1)
    first_profit = await percentage_of_income_for_period(year=answer1, month=answer2, category=3)
    second_profit = await percentage_of_income_for_period(year=answer1, month=answer2, category=4)
    third_profit = await percentage_of_income_for_period(year=answer1, month=answer2, category=2)
    end_profit = await percentage_of_income_for_period(year=answer1, month=answer2, category=5)
    inspection_profit = await percentage_of_income_for_period(year=answer1, month=answer2, category=6)
    unknown_profit = await percentage_of_income_for_period(year=answer1, month=answer2, category=7)
    measuring_profit = await percentage_of_income_for_period(year=answer1, month=answer2, category=8)
    fore_project_profit_profit = await percentage_of_income_for_period(year=answer1, month=answer2, category=9)
    floorplan_profit = await percentage_of_income_for_period(year=answer1, month=answer2, category=10)
    adv_profit = await percentage_of_income_for_period(year=answer1, month=answer2, category=12)
    architect_profit = await percentage_of_income_for_period(year=answer1, month=answer2, category=11)
    consult_profit = await percentage_of_income_for_period(year=answer1, month=answer2, category=13)
    template = "указанный период"

    await message.answer("<b>ОСНОВНЫЕ ПОКАЗАТЕЛИ:</b>")
    await message.answer(f"Доход за указанный месяц: <b>{profit_current_month}</b> рублей\n"
                         f"Доход за указаный год: <b>{profit_current_year / 1000000}</b> млн. рублей\n"
                         f"Доход за аналогичный период прошлого года: <b>{profit_current_month_last_year}</b> рублей\n"
                         f"Разница в доходах с прошлым годом: <b>{difference}</b> рублей\n"
                         f"Средний доход в месяц за весь период: <b>{avprofit / 1000000}</b> млн. рублей\n\n"
                         f"Доходы с комиссионных за весь период: <b>{int(complectation_profit / 1000000)}</b> млн. рублей\n"
                         f"Доходы с проектов за весь период: <b>{int(project_profit_all / 1000000)}</b> млн. рублей\n"
                         f"Доходы с авторского надзора за весь период: <b>{int(supervision_profit)}</b> рублей\n"
                         f"Доходы с обмеров за весь период: <b>{int(measurements_profit)}</b> рублей\n"
                         f"Доходы с планировки за весь период: <b>{int(floor_plan_profit)}</b> рублей\n\n"
                         f"Доходы с фор-проекта за весь период: <b>{int(fore_project_profit)}</b> рублей\n"
                         f"Весь доход с 2018 года: <b>{int(all_profit) / 1000000}</b> млн. рублей\n"
                         f"Доход с комплектации за {template} <b>{round(comlectation_profit), 0}</b> %\n"
                         f"Доход с проектов за {template} <b>{round(first_profit + second_profit + third_profit + end_profit), 0}</b> %\n"
                         f"Доход с авторского надзора за {template} <b>{round(inspection_profit), 0}</b> %\n\n"
                         f"Доход с обмеров за {template} <b>{round(measuring_profit), 0}</b> %\n"
                         f"Доход с фор-проектов за {template} <b>{round(fore_project_profit_profit), 0}</b> %\n"
                         f"Доход с планировок за {template} <b>{round(floorplan_profit), 0}</b> %\n"
                         f"Прочие доходы за {template} <b>{round(unknown_profit + consult_profit + adv_profit ), 0} </b> % \n\n"
                         f"Доход за {year_now - 5} <b>{round(profit_5_year / 1000000), 2}</b> млн. рублей  \n"
                         f"Доход за {year_now - 4} <b>{round(profit_4_year / 1000000), 2}</b> млн. рублей <b>{round((100 - ((round(profit_4_year / 1000000)) / (round(profit_5_year / 1000000) / 100))) * -1)}</b>% \n"
                         f"Доход за {year_now - 3} <b>{round(profit_3_year / 1000000), 2}</b> млн. рублей <b>{round((100 - ((round(profit_3_year / 1000000)) / (round(profit_4_year / 1000000) / 100))) * -1)}</b>%  \n"
                         f"Доход за {year_now - 2} <b>{round(profit_2_year / 1000000), 2}</b> млн. рублей <b>{round((100 - ((round(profit_2_year / 1000000)) / (round(profit_3_year / 1000000) / 100))) * -1)}</b>% \n"
                         f"Доход за {year_now - 1} <b>{round(profit_1_year / 1000000), 2}</b> млн. рублей <b>{round((100 - ((round(profit_1_year / 1000000)) / (round(profit_2_year / 1000000) / 100))) * -1)}</b>% \n"
                         f"Доход за {year_now - 0} <b>{round(profit_0_year / 1000000), 2}</b> млн. рублей <b>{round((100 - ((round(profit_0_year / 1000000)) / (round(profit_1_year / 1000000) / 100))) * -1)}</b>% \n"
                         )
    await message.answer("<b>ДОХОДЫ ОТ ОСНОВНЫХ КЛИЕНТОВ:</b>")
    await message.answer(f"Общий доход с Виталия Зубера: <b>{zuber_profit / 1000000}</b> млн. рублей\n"
                         f"Общий доход с Телелинского Дмитрия: <b>{(telelinskiy_profit+chadigov_profit) / 1000000}</b> млн. рублей\n"
                         f"Общий доход с Петуховой Екатерины: <b>{petuhova_profit / 1000000}</b> млн. рублей\n"
                         f"Общий доход с Нягу Сергея: <b>{nyagu_profit / 1000000}</b> млн. рублей\n"
                         f"Совокупный доход с ключевых заказчиков: <b>{(petuhova_profit + telelinskiy_profit + zuber_profit + drozdov_profit + zaur_profit + trapezdnikov_profit) / 1000000}</b> млн. рублей\n"
                         f"Общий доход с Астон: <b>{(drozdov_profit + trapezdnikov_profit) / 1000000}</b> млн. рублей",
                         reply_markup=ReplyKeyboardRemove())
    await state.finish()


def register_count_profit(dp: Dispatcher):
    dp.register_message_handler(profit_preview, commands=["profit_counter"], state="*")
    dp.register_message_handler(enter_year, state=Profit_filter.Q1)
    dp.register_message_handler(enter_month, state=Profit_filter.Q2)
