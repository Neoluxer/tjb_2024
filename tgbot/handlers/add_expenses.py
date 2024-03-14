from datetime import datetime  # ok

from aiogram import Dispatcher
from aiogram import types  # ok
from aiogram.dispatcher import FSMContext  # ok

try:
    from tjb_2024.tgbot.misc.expenses import Expenses
    from tjb_2024.tgbot.keyboards.menu import expenses_menu
    from tjb_2024.tgbot.models.commands import add_expenses
except:
    from tgbot.misc.expenses import Expenses
    from tgbot.keyboards.menu import expenses_menu  # ok
    from tgbot.models.commands import add_expenses

DATE = '%d.%m.%Y %H:%M:%S'
Log_path = r"Logs\log.txt"
result = "Записано в журнал" + " " + str(datetime.utcnow().strftime(DATE))


async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено")


async def enter_expenses_description(message: types.Message, state: FSMContext):
    await message.answer("Описание расхода: ")
    await state.set_state(Expenses.Q1)


async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer_1"] = answer
    await message.answer("Категория расхода: ", reply_markup=expenses_menu)
    await state.set_state(Expenses.Q2)


async def answer_q2(message: types.Message, state: FSMContext):
    global searchin_id
    answer3 = message.text
    async with state.proxy() as data:
        data["answer_3"] = answer3

    await message.answer("Сумма расхода (20000): ")
    await state.set_state(Expenses.Q3)


async def answer_q3(message: types.Message, state: FSMContext):
    parameters_dict = {'ФОТ':1,'на рекламу':2,'налоги':3,'прочие расходы':4}
    answer2 = message.text  # Сумма расхода
    if answer2.isdigit():
        async with state.proxy() as data:
            data["answer_2"] = answer2
            answer = data.get("answer_1")  # Описание расхода
            answer3 = data.get("answer_3")  # Категория расхода

        try:
            result_string = f'{str(datetime.now())} Описание расхода: {answer}, Категория расхода: {answer3},Сумма расхода: {answer2}'

            with open('media/files/expenses.txt', 'a', encoding='utf-8') as f:
                f.write(str(result_string) + "\n")
            with open('media/files/expenses.txt', 'r', encoding='utf-8') as r:
                last_line = r.readlines()[-1]
                last_line_f = f'{last_line=}'
            await message.answer(str(last_line_f))
            await add_expenses(description=answer, price=answer2, category=parameters_dict[answer3])
            await state.finish()

        except Exception as e:
            await message.answer(str(e))
            await state.finish()

    else:
        print('is not digit')
        await message.answer("Вы ввели не численное значение\n"
                             "Введите число:")

        await state.set_state(Expenses.Q3)


def register_add_expenses(dp: Dispatcher):
    dp.register_message_handler(cmd_cancel, commands=["cancel"], state="*")
    dp.register_message_handler(enter_expenses_description, commands=["add_expenses"], state="*")
    dp.register_message_handler(answer_q1, state=Expenses.Q1)
    dp.register_message_handler(answer_q2, state=Expenses.Q2)
    dp.register_message_handler(answer_q3, state=Expenses.Q3)
