from datetime import datetime  # ok
from aiogram import Dispatcher
from aiogram import types  # ok
from aiogram.dispatcher import FSMContext  # ok
from aiogram.types import ReplyKeyboardRemove
from tgbot.keyboards.menu import income_menu  # ok
from tgbot.misc.profit import Profit
from tgbot.models.commands import add_profit


DATE = '%d.%m.%Y %H:%M:%S'
Log_path = r"Logs\log.txt"
result = "Записано в журнал" + " " + str(datetime.utcnow().strftime(DATE))

async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено")

async def enter_article_creation(message: types.Message, state: FSMContext):
    await message.answer("Описание дохода: ")
    await state.set_state(Profit.Q1)


async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer_1"] = answer
    await message.answer("Источник дохода: ", reply_markup=income_menu)
    await state.set_state(Profit.Q2)


async def answer_q2(message: types.Message, state: FSMContext):
    answer3 = message.text
    async with state.proxy() as data:
        data["answer_3"] = answer3
    await message.answer("Имя заказчика: ", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Profit.Q3)


async def answer_q3(message: types.Message, state: FSMContext):
    global searchin_id
    answer4 = message.text
    async with state.proxy() as data:
        data["answer_4"] = answer4

    await message.answer("Сумма дохода: ")
    await state.set_state(Profit.Q4)


async def answer_q4(message: types.Message, state: FSMContext):
    answer2 = message.text
    if answer2.isdigit():
        async with state.proxy() as data:
            data["answer2"] = answer2
            answer = data.get("answer_1")  # Источник дохода
            answer3 = data.get("answer_3")  # Категория платежа
            answer4 = data.get("answer_4")  # Имя

        dictionary_of_income = {'Комплектация': 1, '1й платёж дизайн проект': 2,
                                '2й платёж дизайн проект': 4, '3й платёж дизайн проект': 3,
                                'Итоговый платёж дизайн проект': 5, 'Авторский надзор': 6,
                                'Обмеры': 8, 'Фор-проект': 9, 'Планировка': 10, 'Проект дома': 11,
                                'Реклама в Инстаграм': 12, 'Консультации': 13}
        try:
            income_id = dictionary_of_income[answer3]
        except:
            income_id = 0

        try:
            await message.answer('Не забудьте отложить с этой суммы '+str(float(answer2)*30/100)+'рублей')

            await message.answer('<a href="http://192.168.31.150:8000/admin/addprofit/addprofits/">admin panel</a>',parse_mode="HTML")  # Источник дохода

            await add_profit(customer = str(answer4), price = float(answer2), description = str(answer),
                             category = int(1))
            await state.finish()

        except Exception as e:
            await message.answer(str(e))
            await state.finish()



    else:
        print('is not digit')
        await message.answer("Вы ввели не численное значение\n"
                             "Введите число:")

        await state.set_state(Profit.Q4)


def register_add_profit(dp: Dispatcher):
    dp.register_message_handler(cmd_cancel, commands=["cancel"], state="*")
    dp.register_message_handler(enter_article_creation, commands=["add_profit"], state="*")
    dp.register_message_handler(answer_q1, state=Profit.Q1)
    dp.register_message_handler(answer_q2, state=Profit.Q2)
    dp.register_message_handler(answer_q3, state=Profit.Q3)
    dp.register_message_handler(answer_q4, state=Profit.Q4)
