import datetime

from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher import FSMContext
from tgbot.data.config import EXEL_PATH, EXEL_PATH2
from tgbot.keyboards.menu import organisations_menu, units_menu
from tgbot.misc.invoice_states import Test
from tgbot.models.commands import add_invoice

async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено")


async def enter_test(message: types.Message, state: FSMContext):
    if message.from_user.full_name == 'Vladimir Kandalov' or message.from_user.id == 1015129409:
        await message.answer("Вы начали формирование Счета.\n"
                             "Введите Покупателя: ")
        await Test.first()
    else:
        await message.answer("Вы начали формирование Счета.\n"
                             "Введите Покупателя: ")
        await Test.first()


async def answer_q1(message: types.Message, state: FSMContext):
    input_customer = message.text
    async with state.proxy() as data:
        data["answer1"] = input_customer
    await message.answer("Введите Продавца: ", reply_markup=organisations_menu)
    await Test.next()


async def answer_q2(message: types.Message, state: FSMContext):
    input_seller = message.text  # ВВЕЛИ ПРОДАВЦА
    async with state.proxy() as data:
        data["answer2"] = input_seller  # Занесли данные о продавце
    await message.answer("Введите название товара или услуги: ")
    await Test.next()


async def answer_q3(message: types.Message, state: FSMContext):
    input_name_of_product = message.text  # ВВЕЛИ НАЗВАНИЕ ТОВАРА ИЛИ УСЛУГИ
    async with state.proxy() as data:
        data["answer3"] = input_name_of_product
    async with state.proxy() as data:
        answer1 = data.get("answer1")
        answer2 = data.get("answer2")
    await message.answer(f'Покупатель: {answer1}\n'
                         f'Продавец: {answer2}\n'
                         f'Услуга: {input_name_of_product}')
    await message.answer("Введите количество товара или услуги: ")
    await Test.next()


async def answer_q4(message: types.Message, state: FSMContext):
    quantity = message.text  # ВВЕЛИ КОЛЛИЧЕСТВО
    if quantity.isdigit():
        async with state.proxy() as data:
            data["answer4"] = quantity
    else:
        await message.answer("Вы ввели не численное значение\n"
                             "Введите число:")
        await Test.previous()
    async with state.proxy() as data:
        answer1 = data.get("answer1")
        answer2 = data.get("answer2")
        answer3 = data.get("answer3")

    await message.answer(f'Покупатель: {answer1}\n'
                         f'Продавец: {answer2}\n'
                         f'Услуга: {answer3}\n'
                         f'Количество: {quantity}\n ')
    await message.answer("Введите цену за 1 ед. изм.: ")
    await Test.next()


async def answer_q5(message: types.Message, state: FSMContext):
    price = message.text  # ВВЕЛИ ЦЕНУ
    if price.isdigit():
        async with state.proxy() as data:
            data["answer5"] = price
    else:
        await message.answer("Вы ввели не численное значение\n"
                             "Введите число:")
        await Test.previous()
    async with state.proxy() as data:
        answer1 = data.get("answer1")
        answer2 = data.get("answer2")
        answer3 = data.get("answer3")
        answer4 = data.get("answer4")

    await message.answer(f'Покупатель: {answer1}\n'
                         f'Продавец: {answer2}\n'
                         f'Услуга: {answer3}\n'
                         f'Количество: {answer4}\n'
                         f'Цена за 1 ед.изм.:{price} рублей\n ')
    await message.answer("Введите единицу измерения (м.кв.,шт.): ", reply_markup=units_menu)
    await Test.next()


async def answer_q6(message: types.Message, state: FSMContext):
    from tgbot.models.invoice_class import Invoice
    from invoice.models import Invoice as invoiceModel
    try:
        number_of_last_invoice = invoiceModel.objects.latest('id')
        number_1 = (int(number_of_last_invoice.id)) + 1
    except:
        number_1 = 1
    unit = message.text  # ВВЕЛИ Ед.изм.
    async with state.proxy() as data:
        answer1 = data.get("answer1")
        answer2 = data.get("answer2")
        answer3 = data.get("answer3")
        answer4 = data.get("answer4")
        answer5 = data.get("answer5")

    await message.answer("Счет и Акт сформирован!")
    summa = int(answer5) * int(answer4)


    # Путь и название файла для формирования акта:
    wb_filename_akt = f'{EXEL_PATH}akt_{summa}_{number_1}.xlsx'
    # Путь и название файла для формирования счета:
    wb_filename_invoice = f'{EXEL_PATH}invoice_{summa}_{number_1}.xlsx'
    name_of_akt = number_1
    name_of_invoice = number_1
    new_akt = await Invoice(customer=str(answer1),
                            executor=str(answer2),
                            name_of_services=str(answer3),
                            quantity=int(answer4),
                            price=int(answer5),
                            units=str(unit),
                            number_akt=name_of_akt,
                            )

    new_akt.exel_generator_akt()
    new_akt.exel_generator()
    print(f'number_akt = {new_akt.number_akt}')
    await add_invoice(name=str(answer3),
                      published=datetime.date.today(),
                      sum=summa,
                      invoice_number=name_of_invoice,
                      invoice_file=f'{EXEL_PATH}akt_{summa}_{number_1}.xlsx',
                      invoice_file_invoice=f'{EXEL_PATH}invoice_{summa}_{number_1}.xlsx',
                      )
    print(f'name_of_invoice = {new_akt.name_of_invoice}')
    with open(f'{EXEL_PATH2}invoice_{summa}_{number_1}.xlsx', 'rb') as docx_file:  # Открывает и отправляет в бот
        await message.answer_document(docx_file)
    await message.answer('<a href="http://127.0.0.1:8000/admin/invoice/invoice/">admin panel</a>',
                         parse_mode="HTML")
    await state.finish()  # Сбрасывается состояние и сбрасываются данные


def register_add_invoice(dp: Dispatcher):
    dp.register_message_handler(cmd_cancel, commands=["cancel"], state="*")
    dp.register_message_handler(enter_test, commands=["invoice"], state="*")
    dp.register_message_handler(answer_q1, state=Test.Q1)
    dp.register_message_handler(answer_q2, state=Test.Q2)
    dp.register_message_handler(answer_q3, state=Test.Q3)
    dp.register_message_handler(answer_q4, state=Test.Q4)
    dp.register_message_handler(answer_q5, state=Test.Q5)
    dp.register_message_handler(answer_q6, state=Test.Q6)


